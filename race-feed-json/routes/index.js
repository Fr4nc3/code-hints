"use strict";
var express = require('express');
var router = express.Router();
var axios = require('axios');
var dal = require('../dataLayer');
/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index', {
    title: 'Express'
  });
});
var URL = 'http://ori-nodeassets.nbcnews.com/elections/2018-05-08/races_S_counties.json';

router.get('/races/:variable*?', function (req, res, next) {
    axios.get(URL).then(function (response) {  
      res.json(dal.apiRaces(req.params.variable, response.data));
    });

});
router.get('/candidates/:variable*?', function (req, res, next) {
    axios.get(URL).then(function (response) {
      res.json(dal.apiCandidates(req.params.variable, response.data));
    });
});
router.get('/counties/:variable*?', function (req, res, next) {
  axios.get(URL).then(function (response) {
    res.json(dal.apiCounties(req.params.variable, response.data));
  });
});

module.exports = router;
