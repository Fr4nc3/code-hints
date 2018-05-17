angular.module('myApp')
.controller('dashboardCtrl', ['$scope', 'DataService', function($scope, DataService) {

    $scope.lineTotalDaily = {};
    $scope.lineTotalDaily.labelX = "Date";
    $scope.lineTotalDaily.labelY = "# Items Sold";
    $scope.lineTotalDaily.guidelinesX = false;
    $scope.lineTotalDaily.guidelinesY = true;
    $scope.lineTotalDaily.formatY = "f";
    $scope.lineTotalDaily.legend = "bottom";
    DataService.getDailyTotal().then(function(data) {
        console.log("Data here", data.data);
        $scope.lineTotalDaily.data = [{key: "Sales", values: data.data}];
    }).catch(function(err) {
        console.error("There was an error");
    })
    $scope.lineAverageDaily = {};
    $scope.lineAverageDaily.labelX = "Date";
    $scope.lineAverageDaily.labelY = "# AVG Items Sold";
    $scope.lineAverageDaily.guidelinesX = false;
    $scope.lineAverageDaily.guidelinesY = true;
    $scope.lineAverageDaily.formatY = "f";
    $scope.lineAverageDaily.legend = "bottom";
    DataService.getDailyAvg().then(function(data) {
        console.log("Data", data.data);
        $scope.lineAverageDaily.data = [{key: "Sales", values: data.data}];
    }).catch(function(err) {
        console.error("There was an error");
    })

    $scope.lineTotalPerItem = {};
    $scope.lineTotalPerItem.labelX = "Date";
    $scope.lineTotalPerItem.labelY = "# Items Per itemsSold";
    $scope.lineTotalPerItem.guidelinesX = false;
    $scope.lineTotalPerItem.guidelinesY = true;
    $scope.lineTotalPerItem.formatY = "f";
    $scope.lineTotalPerItem.legend = "bottom";
    DataService.getDailyPerItem().then(function(data) {
        console.log("Data", data.data);
        $scope.lineTotalPerItem.data = [{key: "Dani", values: data.data[0]},{key: "Milki", values: data.data[1]},  ];
    }).catch(function(err) {
        console.error("There was an error");
    })

}])
