var myApp = angular.module('myApp', ['ui.router', 'ngMaterial', 'ngResource', 'charts', 'ngCookies', 'chart.js', 
'nvd3', 'ngMessages', 'angularUtils.directives.dirPagination']);//task001

myApp.config(['$stateProvider', '$urlRouterProvider', '$locationProvider', function ($stateProvider, $urlRouterProvider, $locationProvider) {

    // var defaultState = { state: "dash.authenticated.sandbox", params: null };
    var defaultState = "dash.authenticated.dashboard";

  	$locationProvider.html5Mode({
  		enabled: true,
  		requireBase: false
  	});

	// for unmatched urls, redirect
  	$urlRouterProvider.otherwise('/dashboard');

    // abstract state handles preloading of config dependencies, redirect to disabled state, and title changes (do not remove)
    $stateProvider.state('dash', {
        abstract: true,
        resolve: {
            defaultState: function() { return defaultState; }
        },
        controller: 'abstractStateCtrl',
        template: '<ui-view/>'
    });

    $stateProvider.state('dash.dashboard', {
        title: 'Dashboard',
        icon: 'dashboard',
        url: '/dashboard',
        family: 'dashboard',
        controller: 'dashboardCtrl',
        templateUrl: '/states/dashboard.html'
    });
}]);
