/**
 * Created by hcassus on 9/17/15.
 */
var app = angular.module("pedidoApp", []);
app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});