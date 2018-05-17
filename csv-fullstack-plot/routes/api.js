var express = require('express');
var router = express.Router();
var dal = require('../dataAccessLayer');

var loader = require('csv-load-sync');

// a data api
router.get('/example', function(req, res) {
    dal.getExampleItemData()
    .then(function(result) {
        res.json(result);
    })
    .fail(function(err) {
        res.status(500).send(result);
    })
});

router.get('/data', function(req, res) { // full csv file
    dal.getcsvData()
    .then(function(result) {
        res.json(result);
    })
    .fail(function(err) {
        res.status(500).send(result);
    })
});
router.get('/getDailyTotal', function(req, res) {
    dal.getDailyTotal()
    .then(function(result) {
        res.json(result);
    })
    .fail(function(err) {
        res.status(500).send(result);
    })
});
router.get('/getDailyAvg', function(req, res) {
    dal.getDailyAvg()
    .then(function(result) {
        res.json(result);
    })
    .fail(function(err) {
        res.status(500).send(result);
    })
});
router.get('/getDailyPerItem', function(req, res) {
    dal.getDailyPerItem()
    .then(function(result) {
        res.json(result);
    })
    .fail(function(err) {
        res.status(500).send(result);
    })
});

module.exports = router;