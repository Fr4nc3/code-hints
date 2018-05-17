var express = require('express');
var path = require('path');
var fs = require('fs');
var logger = require('./common/loggingHandler').logger;
var loader = require('csv-load-sync');
// routing
var routes = require('./routes/index');

// api
var api = require('./routes/api');

// express server
var app = express();

app.enable('trust proxy');

// load global configurations
require('./config');

// view engine setup
app.set('views', path.join(__dirname, './ui/common/main_page'));
app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname, './ui')));
app.use('/ui', express.static(path.join(__dirname, './ui')));
app.use('/bower_components',  express.static(path.join(__dirname, '/bower_components')));
app.use('/', routes);
app.use('/api', api);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// production error handler, no stacktraces leaked to user
if (app.get('env') === 'production') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: {}
        });
    });
}

// development error handler, will print stacktrace
else {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

module.exports = app;
