myApp.factory('DataService', ['$http', function($http) {
    
    // App configurations
    var getExampleData = function() {
        return $http.get("/api/example", null);
    };
    var getcsvData = function() {
        return $http.get("/api/data", null);
    };
    var  getDailyTotal = function() {
        return $http.get("/api/getDailyTotal", null);
    };
    var  getDailyAvg = function() {
        return $http.get("/api/getDailyAvg", null);
    };
    var   getDailyPerItem = function() {
        return $http.get("/api/getDailyPerItem", null);
    };
    return {
        // app and them configurations
        getExampleData: getExampleData,
        getcsvData: getcsvData,
        getDailyTotal: getDailyTotal,
        getDailyAvg:  getDailyAvg,
        getDailyPerItem:  getDailyPerItem
    };

}]);