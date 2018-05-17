require('../config');

try {
    var log4js = require('log4js');
    log4js.configure(global_config.loggingConfig.config);
    var logger = log4js.getLogger('app');
    logger.setLevel(global_config.loggingConfig.level);
}
catch(e) {
    // if log4js not installed, use default node console
    var logger = console;
}

module.exports = {
    logger: logger
};