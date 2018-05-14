"use strict";
/*
API connection variables
*/
const TUMBLR_KEY = "";
const GOOGLE_KEY = "";
const GOOGLE_CX = "";

const TUMBLR_URL = `https://api.tumblr.com/v2/tagged?api_key=${TUMBLR_KEY}&tag=`;
const GOOGLE_URL = `https://www.googleapis.com/customsearch/v1?key=${GOOGLE_KEY}&cx=${GOOGLE_CX}&alt=json&searchType=image&q=`;

/**
 * Gets the API call 
 *
 * @method onSearch
 *
 * @param  {object} value DOM object
 * 
 */
function onSearch(value) {
    var el = document.getElementById('searchterm');
    if (el.value.length < 3) {
       errorMessage("Error Alert!", "Add a word of 3 characters or more!");
        return false;
    }
    var engine = document.querySelector('input[name="engine"]:checked').value;
    var url = (engine == "google" ? GOOGLE_URL : TUMBLR_URL) + el.value;
    var success = engine == "google" ? googleSuccess : tumblrSuccess;
    getCORS(url, function (request) {
        var response = request.currentTarget.response || request.target.responseText;
        success(JSON.parse(response));
    });

};

/**
 * Create the object for the error popup modal
 * @method errorMessage
 *
 * @param  {string} errorHeader
 * @param  {string} errorBody
 * 
 */
function errorMessage(errorHeader, errorBody){
    var header = document.createElement('span');
    var body = document.createElement('div');
    header.className = "alert-header";
    body.className = "alert-body";
    header.innerHTML = errorHeader;
    body.innerHTML = errorBody;
    openModal(header, body);

};
/**
 * prepare the modal popup
 * @method openModal
 *
 * @param  {string} header
 * @param  {string} body
 * 
 */
function openModal(header, body) {
    var overlay = document.getElementById('overlay');
    var modalBody = document.getElementById('modalBody');
    var modalHeading = document.getElementById('modalHeading');
    empty(modalBody);
    empty(modalHeading);
    modalHeading.appendChild(header);
    modalBody.appendChild(body);
    overlay.classList.remove("is-hidden");
};
/**
 * Close modal popup
 * 
 * @method closeModal
 * 
 */
function closeModal() {
    var overlay = document.getElementById('overlay');
    overlay.classList.add("is-hidden");
};
/**
 * Cross - origin resource sharing ajax
 * @method getCORS
 *
 * @param  {string} url
 * @param  {method} sucess
 * @return {Request} object
 */
function getCORS(url, success) {
    var xhr = new XMLHttpRequest();
    if (!('withCredentials' in xhr)) xhr = new XDomainRequest(); // fix IE8/9
    xhr.open('GET', url);
    xhr.onload = success;
    xhr.send();
    return xhr;
};

/**
 * Parse tumblr api response
 * @method tumblrSuccess
 *
 * @param  {object} data
 * 
 */
function tumblrSuccess(data) {
    var list = data.hasOwnProperty("response") ? data.response.filter(x => x.type == "photo").map(x => ({
        images: [{
            caption: x.caption,
            originalSize: x.photos[0].original_size.url,
            sizes: x.photos[0].alt_sizes.map(p => ({
                width: p.width,
                url: p.url
            }))
        }]
    })) : [];
    populate(list);
};

/**
 * Parse google api response
 * @method googleSuccess
 *
 * @param  {object} data
 * 
 */
function googleSuccess(data) {
    var list = data.hasOwnProperty("items") ? data.items.map(x => ({
        images: [{
            caption: x.title,
            originalSize: x.link,
            sizes: [{
                    width: x.image.thumbnailWidth,
                    url: x.image.thumbnailLink
                },
                {
                    width: x.image.width,
                    url: x.link
                }
            ]
        }]
    })) : [];
    populate(list);

};

/**
 * empty dom object
 * @method  empty
 *
 * @param  {object} el
 * 
 */
function empty(el){
    while (el.firstChild) el.removeChild(el.firstChild)
};

/**
 *  Populete div results
 * @method populate
 *
 * @param  {array} list
 * 
 */
function populate(list) {
    var insertionPoint = document.getElementById("results");
    empty(insertionPoint);
    if(list.length == 0){
        errorMessage("Alert!", "No Results!");
        return false;
    }
    var layout = buildLayoutFromRows(list);

    insertionPoint.appendChild(layout);
};

/**
 *  handle html DOM click 
 *
 * @param  {object} data
 * 
 */
document.addEventListener("click", function (e) {
    var target = e.target;

    while (target && target.parentNode !== document) {
        target = target.parentNode;
        if (!target) {
            return;
        }
        if (target.classList.contains('modal-content')){
            closeModal();
        }
        if (target.classList.contains('item')) {
            imageModal(target);
        }
    }
});

/**
 * prepare image to the modal popup
 * @method imageModal
 * @param  {object} el
 * 
 */
function imageModal(el){
    var body = el.getElementsByTagName('img')[0].cloneNode(true);
    var header = el.getElementsByTagName('span')[0].cloneNode(true);
    header.classList.remove("is-hidden");
    openModal(header, body);
}; 

/**
 * create image from search results
 * @method getImageElement
 *
 * @param  {object} image
 * @param  {int} totalCount
 * @return {object} item
 * 
 */
function getImageElement(image, totalCount) {
    return `<div class="item"><img src=${image.originalSize} srcset="${image.sizes.map(({url, width}) => `
    $ {
        url
    }
    $ {
        width
    }
    w `).join(', ')}" sizes="(max-width: ${1636 / totalCount}px) ${100 / totalCount}vw, ${540 / totalCount}px" /><span class="is-hidden">${image.caption}</span></div>`;
};

/**
 * create div row from the results
 * @method buildRowFromImages
 *
 * @param  {array} image
 * @return {object} row
 * 
 */
function buildRowFromImages(images) {
    return `<div class="row">${images.map((image) => getImageElement(image, images.length)).join('')}</div>`;
};

/**
 * create div layout from the api results
 * @method buildLayoutFromRows
 *
 * @param  {array} rows
 * @return {object} layout
 * 
 */
function buildLayoutFromRows(rows) {
    const template = document.createElement('template');
    template.innerHTML = `<div class="layout">${rows.map((row) => buildRowFromImages(row.images)).join('')}</div>`
    return template.content.firstChild;
};