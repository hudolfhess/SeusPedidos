/**
 * Created by hcassus on 9/17/15.
 */
app.controller("clienteCtrl", function($scope) {

    $scope.clientes = [
        {nome:'Henrique Cassus',email:'henrique.cassus@meuspedidos.com.br'},
        {nome:'Juan Ramires',email:'juan@meuspedidos.com.br'},
        {nome:'Jonathan Welzel',email:'jonathan.welzel@meuspedidos.com.br'},
        {nome:'Hudolf Hess',email:'hudolf@meuspedidos.com.br'}
    ];

    $scope.adicionaCliente  = function() {
        cliente = $scope.cliente;
        $scope.clientes.push(cliente);
        $scope.cliente = {};
    };

    $scope.removerCliente = function(index) {
        $scope.clientes.splice(index,1);
    }



});