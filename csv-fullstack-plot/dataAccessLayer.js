var Q = require('q');
var fs = require("fs");
var loader = require('csv-load-sync');
var alasql = require('alasql');
var csv = loader('data/data.csv');

csv = csv.map((c, index, csv) => {
    return {
       a: parseInt(c.count),
       mydate: c.date, 
       item: c.item
    };
});

var getExampleItemData = function() {
    var deferred = Q.defer();
    
    var result = [
        {key: "2016-06-02", values: 10},
        {key: "2016-06-03", values: 15},
        {key: "2016-06-04", values: 16},
        {key: "2016-06-05", values: 17},
        {key: "2016-06-06", values: 25},
        {key: "2016-06-07", values: 5},

    ];

    deferred.resolve(result);

    return deferred.promise;
}

var getcsvData = function() { // full data as example
    var deferred = Q.defer();
    //customerId, item, count, date
    // alasql('SELECT item, SUM(a) AS b, mydate FROM ? GROUP BY item, mydate',[csv]);
    var result = csv;
    deferred.resolve(result);

    return deferred.promise;
}
var createData = function(res){
 return res.map((r, index, res) => {
     return {
         values: r.b,
         key: r.mydate
     };
 })


}
// 1) Total daily pudding items sold
var getDailyTotal = function() {
    var deferred = Q.defer();
    //customerId, item, count, date
    var res = alasql('SELECT SUM(a) AS b, mydate as mydate FROM ? GROUP BY  mydate',[csv]);
    res = createData(res);
    deferred.resolve(res);

    return deferred.promise;
}
//Average daily pudding items sold per customer
var getDailyAvg = function() {
    var deferred = Q.defer();
    //customerId, item, count, date
    var res = alasql('SELECT AVG(a) AS b, mydate as mydate FROM ? GROUP BY  mydate',[csv]);
    // trick to format my response as expected / key/ values 
    res = createData(res);
    deferred.resolve(res);

    return deferred.promise;
}
//3) Total daily item sales, split into a line for each pudding item (Jonny, Molly etc)
var getDailyPerItem = function() {
    var deferred = Q.defer();
    //customerId, item, count, date
    var res = alasql('SELECT SUM(a) AS b, mydate, item FROM ? GROUP BY  item, mydate',[csv]);
    var jonny = alasql('SELECT  b, mydate FROM ? where item == "Jonny"', [res]);
    var molly = alasql('SELECT  b, mydate FROM ? where item == "Molly"', [res]);
    // this is pretty much a very un optimized way to create the two results and return them
    // this is because alassql doesn't accept key/values as field names 
    jonny =  createData(jonny);
    molly =  createData(molly);
    var result = [jonny, molly];
    deferred.resolve(result);

    return deferred.promise;
}
module.exports = {
    // export methods here
    getExampleItemData: getExampleItemData,
    getcsvData: getcsvData,
    getDailyTotal: getDailyTotal,
    getDailyAvg: getDailyAvg,
    getDailyPerItem: getDailyPerItem
};
