var express = require('express');
var router = express.Router();

var stateRenderFunction = function(req, res, next) {
  res.render('index', {});
}

router.get('/', stateRenderFunction);
router.get('/dashboard', stateRenderFunction);

module.exports = router;
