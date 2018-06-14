var Q = require('q');
var rp = require('request-promise');
var http = require('http');
const apiRaces = (variable, body) => {
    var deferred = Q.defer();
console.log("here");
    let result = {
        "id": 1
    };
    deferred.resolve(result);
    return deferred.promise;
};
const apiCandidates = (variable, body) => {

    var deferred = Q.defer();

    let result = {
        "id": 1
    };
    deferred.resolve(result);
    return deferred.promise;
};
const apiCounties = (variable, body) => {
    return {
        id: 1
    };
};

var loadBody = function (res) {
    var deferred = Q.defer();
    var body = "";
    res.on("data", function (chunk) {
        body += chunk;
    });
    res.on("end", function () {
        deferred.resolve(body);
    });
    return deferred.promise;
};

const httpGet = function (opts) {
     var deferred = Q.defer();
     http.get(opts, deferred.resolve);
     return deferred.promise;
};
module.exports = {
    // export methods here
    httpGet: httpGet,
    apiRaces: apiRaces,
    loadBody: loadBody

};