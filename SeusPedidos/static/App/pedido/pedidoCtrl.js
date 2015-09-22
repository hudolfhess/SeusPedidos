/**
 * Created by hcassus on 9/17/15.
 */
app.controller("pedidoCtrl", function($scope, $http) {

    $scope.pedidos = [];
    $scope.clientes = [];
    $scope.produtos = [];

    $scope.pedido = {cliente: undefined, cliente_id: 0, itens: []};

    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

    $scope.carregarPedidos = function() {
        return requests(
            $http,
            '/api/pedido',
            'get',
            null,
            function (r) {
                for (i = 0; i < r.data.length; i++) {
                    $scope.pedidos[i] = r.data[i];
                }
            }
        );
    };

    $scope.carregarClientes = function() {
        return requests(
            $http,
            '/api/cliente',
            'get',
            null,
            function (r) {
                for (i = 0; i < r.data.length; i++) {
                    $scope.clientes[i] = sanitizeRequestData(r.data[i]);
                }
            }
        );
    };

    $scope.carregarProdutos = function() {
        return requests(
            $http,
            '/api/produto',
            'get',
            null,
            function (r) {
                for (i = 0; i < r.data.length; i++) {
                    $scope.produtos[i] = sanitizeRequestData(r.data[i]);
                }
            }
        );
    };

    $scope.gerarPedido  = function() {
        requests(
            $http,
            '/api/pedido',
            'post',
            $scope.pedido,
            function(r) {
                $('form .form-group').removeClass('has-error');
                if (r.data.success == 1) {
                    window.location = '/pedido';
                }
                showMessage(r);
            }
        );
    };

    $scope.removerPedido = function(index) {
        $scope.pedidos.splice(index,1);
    };

    /*
    $scope.editarPedido = function(index){
        $scope.pedido = pedidos[index];
    };

    $scope.salvarAlteracoes = function(index){
        $scope.pedidos[index] = $scope.pedido;
    };
    */

    $scope.adicionarItem = function(){
        $scope.item.produto = $scope.produtos[$scope.index_produto]
        item = $scope.item;
        $scope.pedido.itens.push(item);
        $scope.item = {};
    };

    $scope.removerItem = function(index, nome) {
        if (confirm("Remover o produto " + nome + "?")) {
            $scope.pedido.itens.splice(index, 1);
        }
    };

    $scope.carregarPedidos();
    $scope.carregarClientes();
    $scope.carregarProdutos();

});