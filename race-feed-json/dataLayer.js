var Q = require('q');
var rp = require('request-promise');
const apiRaces = (variable, body) => {

   var races = variable ? body.races.filter(x => x.race_name === variable) : body.races;
   return races.map((c, index, body) => {
       return {
           race_id: c.race_id,
           election_date: c.election_date,
           party: c.party,
           state_name: c.state_name,
           total_vote: c.total_vote,
           percent_in: c.percent_in

       };
   });



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

module.exports = {
    // export methods here
    apiRaces: apiRaces,

};