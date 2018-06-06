var mongoose = require('mongoose');
var crypto = require('crypto');
var jwt = require('jsonwebtoken');

var UserSchema = new mongoose.Schema({
  username: {type: String, lowercase: true, unique: true},
  hash: String,
  salt: String
});

UserSchema.methods.validPassword = function(password) {
  //var hash = crypto.pbkdf2Sync(password, this.salt, 1000, 64).toString('hex');
 var hash = crypto.pbkdf2Sync(password, 'salt', 10000, 64, 'sha512').toString('base64');
  return this.hash === hash;
};

UserSchema.methods.setPassword = function(password){
 // this.salt = crypto.randomBytes(16).toString('hex');
  this.hash= crypto.pbkdf2Sync(password, 'salt', 10000, 64, 'sha512').toString('base64');
  //this.hash = crypto.pbkdf2Sync(password, this.salt, 1000, 64).toString('hex');
};

UserSchema.methods.generateJWT = function() {

  // set expiration to 60 days
  var today = new Date();
  var exp = new Date(today);
  exp.setDate(today.getDate() + 60);

  return jwt.sign({
    _id: this._id,
    username: this.username,
    exp: parseInt(exp.getTime() / 1000),
  }, 'SECRET');
};

mongoose.model('User', UserSchema);