angular.module("myApp")
.service('HttpMiddlewareService', ['$q', '$log', function($q,$log) {
    //$log.debug('$log is here to show you that this is a regular factory with injection');

    this.responseRouter = {};
    this.setResponseRouter  = function(resRouter){
            this.responseRouter = resRouter;
    };

    this.response = function(response){
            //response.status - status code (200, 201, etc)
            //Check whether the status code exists in the responseRouter provider. if so - executes the relevant function.
            if (response.status in this.responseRouter){
                this.responseRouter[response.status].fn(response);
            }
            return response;
        };

    this.responseError=function(error){
        //error.status
        //Check whether the status code exists in the responseRouter provider. if so - executes the relevant function.
        if (error.status in this.responseRouter){
            this.responseRouter[error.status].fn(error);
        }
            return $q.reject(error);
        };

    //intercept a request before it is sent.
    this.request = function(config){
            //Set the header to contain the auth token.
            return config;
        };

    this.requestError=function(error){
            return $q.reject(error);
        };
}]);

myApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.interceptors.push('HttpMiddlewareService');
    //enable caching; TODO: needs to be tested and validated.
    $httpProvider.defaults.cache = true;
}]);

//an example of how HttpMiddlewareService should be configured from outside the code to handle various status codes.
//Notice you can inject different service and have them references within the anonymous functions. A sample usecase will be inject some sort
// of popup service and show a popup over $rootscope when an error is received.
myApp.run(['$q', '$log', 'HttpMiddlewareService', '$state', function ($q, $log, HttpMiddlewareService, $state) {

    responseRouter = {};
    responseRouter["200"] = {"fn":{}};
    responseRouter["200"]["fn"] = function(response){
        $log.info("request was successful");
    };

    responseRouter["401"] = {"fn":{}};
    responseRouter["401"]["fn"] = function(response){
        $log.error("request was unauthorized");
    };

    responseRouter["404"] = {"fn":{}};
    responseRouter["404"]["fn"] = function(response){
        $log.error("request was errornous");
    };

    responseRouter["500"] = {"fn":{}};
    responseRouter["500"]["fn"] = function(response){
        $log.error("server error");
    };

    HttpMiddlewareService.setResponseRouter(responseRouter);
}]);
