/**
 * Created by hcassus on 9/17/15.
 */
app.controller("pedidoCtrl", function($scope) {

    $scope.clientes = [
        {id:1, nome:'Henrique Cassus',email:'henrique.cassus@meuspedidos.com.br'},
        {id:2, nome:'Juan Ramires',email:'juan@meuspedidos.com.br'},
        {id:3, nome:'Jonathan Welzel',email:'jonathan.welzel@meuspedidos.com.br'},
        {id:4, nome:'Hudolf Hess',email:'hudolf@meuspedidos.com.br'}
    ];

    $scope.pedido = {cliente:undefined, itens:[]};

    $scope.pedidos = [{id:1, cliente:'Henrique Cassus' ,total:150.00, status:'Concluido'}];

    $scope.produtos = [
        {id:1, nome:"Produto Teste", valor:50.00},
        {id:2, nome:"Produto Teste 1", valor:60.00},
        {id:3, nome:"Produto Teste 2", valor:80.00}
    ];

    $scope.gerarPedido  = function() {
        $scope.pedido.cliente = $scope.clientes[$scope.index_produto]
        pedido = $scope.pedido;
        $scope.pedidos.push(pedido);
        $scope.pedido = {};
    };

    $scope.removerPedido = function(index) {
        $scope.pedidos.splice(index,1);
    };

    $scope.adicionarItem = function(){
        $scope.item.produto = $scope.produtos[$scope.index_produto]
        item = $scope.item;
        $scope.pedido.itens.push(item);
        $scope.item = {};
    };

    $scope.editarPedido = function(index){
        $scope.pedido = pedidos[index];
    }

    $scope.salvarAlteracoes = function(index){
        $scope.pedidos[index] = $scope.pedido;
    }

});