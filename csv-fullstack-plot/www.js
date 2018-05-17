var app = require('./server-app');
var http = require('http');
var env = process.env.NODE_ENV || 'development';

// load global configurations
require('./config');

// get port from environment and store in Express
function randPort() {
    return Math.floor((Math.random() * 1000) + 2000);
}

var randomPort = randPort()
var port = normalizePort(process.env.PORT || 2000);
app.set('port', port);

console.info("Running on port", port);

// create HTTP server
var server = http.createServer(app);

server.listen(port);
server.on('error', function(e) {
    e.message = 0
    return onError(e)
});
server.on('listening', onListening);

// normalize a port into a number, string, or false
function normalizePort(val) {
    var port = parseInt(val, 10);

    if (isNaN(port)) {
        // named pipe
        return val;
    }

    if (port >= 0) {
        // port number
        return port;
    }

    return false;
}

// event listener for HTTP server "error" event
function onError(error) {

    if (error.syscall !== 'listen') {
        throw error;
    }

    var bind = typeof port === 'string' ? 'Pipe ' + port : 'Port ' + port;

    // handle specific listen errors with friendly messages
    switch (error.code) {
        case 'EACCES':
            console.error(bind + ' requires elevated privileges');
            process.exit(1);
            break;
        case 'EADDRINUSE':
            var counter = error.message + 1
            if (counter < 1000) {
                randomPort = randPort();

                port = normalizePort(process.env.PORT || randomPort);
                app.set('port', port);
                console.warn("Port Occupied. Running on port", port);

                // Create HTTP server.

                server = http.createServer(app);
                server.listen(port);
                server.on('error', function(e) {
                    e.message = counter
                    return onError(e)});
                server.on('listening', onListening);
                break;
            }
            else {
                console.error("Ports full")
                process.exit(1);
                break;
            }
        default:
            throw error;
    }
}

// event listener for HTTP server "listening" event
function onListening() {
    var addr = server.address();
    var bind = typeof addr === 'string' ? 'pipe ' + addr : 'port ' + addr.port;
}