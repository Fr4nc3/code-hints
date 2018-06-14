var express = require('express');
var router = express.Router();
var dal = require('../dataLayer');
var url = require("url");
/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index', {
    title: 'Express'
  });
});
var URL = 'http://ori-nodeassets.nbcnews.com/elections/2018-05-08/races_S_counties.json';

const apiRaces = (variable, body) => {
  // var deferred = Q.defer();
  // console.log("here");
  // let result = {
  //   "id": 1
  // };
  // deferred.resolve(result);
  // return deferred.promise;
  return "h";
};

router.get('/races/:variable*?', function (req, res, next) {

       dal.httpGet(url.parse(URL))
        // .then(function (res) {
        //   return dal.loadBody(res);
        // }).then(function (body) {
        //    return res;
        .then(function (res) {
          res.json("edit");
        });


});
router.get('/candidates/:variable*?', function (req, res, next) {
  res.json(getApi(req.params.variable, apiCandidates));
});
router.get('/counties/:variable*?', function (req, res, next) {
  res.json(getApi(req.params.variable, apiCounties));
});

module.exports = router;
