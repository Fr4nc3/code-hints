require('../config');

var errors = global_config.errors;

var getError = function(errName) {
    return errors[errName];
}

module.exports = {
    getError: getError
};