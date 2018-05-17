var Q = require('q');
var fs = require("fs");
var loader = require('csv-load-sync');
var alasql = require('alasql');
var csv = loader('data/data.csv');
for (var i in csv) {
    csv[i].a = parseInt(csv[i].count);
    csv[i].mydate = csv[i].date;
}
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

var MyData = []; 

var getcsvData = function() { // full data as example
    var deferred = Q.defer();
    //customerId, item, count, date
    // alasql('SELECT item, SUM(a) AS b, mydate FROM ? GROUP BY item, mydate',[csv]);
    var result = csv;

    deferred.resolve(result);

    return deferred.promise;
}
// 1) Total daily pudding items sold
var getDailyTotal = function() {
    var deferred = Q.defer();
    //customerId, item, count, date
    var res = alasql('SELECT SUM(a) AS totalSales, mydate as mydate FROM ? GROUP BY  mydate',[csv]);
    for (var i in res) {
        res[i].values =  res[i].totalSales;
        res[i].key =  res[i].mydate;
        delete res[i].totalSales;
        delete  res[i].mydate;
      }
    deferred.resolve(res);

    return deferred.promise;
}
//Average daily pudding items sold per customer
var getDailyAvg = function() {
    var deferred = Q.defer();
    //customerId, item, count, date
    var res = alasql('SELECT AVG(a) AS avgSales, mydate as mydate FROM ? GROUP BY  mydate',[csv]);
    // trick to format my response as expected / key/ values 
    for (var i in res) {
        res[i].values =  res[i].avgSales;
        res[i].key =  res[i].mydate;
        delete res[i].avgSales;
        delete  res[i].mydate;
    }
    deferred.resolve(res);

    return deferred.promise;
}
//3) Total daily item sales, split into a line for each pudding item (Dani, Milki etc)
var getDailyPerItem = function() {
    var deferred = Q.defer();
    //customerId, item, count, date
    var res = alasql('SELECT SUM(a) AS totalSales, mydate,item FROM ? GROUP BY  item,mydate',[csv]);

    var dani = alasql('SELECT  totalSales, mydate FROM ? where item == "Dani"',[res]);
    var milki = alasql('SELECT  totalSales, mydate FROM ? where item == "Milki"',[res]);
    // this is pretty much a very un optimized way to create the two results and return them
    // this is because alassql doesn't accept key/values as field names 
    // and I wouldn't change the key/values names to create the linechart in the controller 
    for (var i in dani) {
        dani[i].values =  dani[i].totalSales;
        dani[i].key =  dani[i].mydate;
        delete dani[i].totalSales;
        delete dani[i].mydate;
      }
      for (var i in milki) {
        milki[i].values =  milki[i].totalSales;
        milki[i].key =  milki[i].mydate;
        delete milki[i].totalSales;
        delete milki[i].mydate;
      }
    var result = [dani, milki];
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
