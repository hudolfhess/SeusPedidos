/**
 * Created by hcassus on 9/17/15.
 */
app.controller("produtoCtrl", function($scope, $http) {

    $scope.produtos = [];

    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

    $scope.carregar = function() {
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

    $scope.adicionaProduto = function() {
        /*
        var requestMethod = 'post';
        if (typeof $scope.produto != 'undefined' && typeof $scope.produto.id != 'undefined') {
            requestMethod = 'put';
        }
        */
        requests(
            $http,
            '/api/produto',
            'post',
            $scope.produto,
            function(r) {
                if (r.data.success == 1) {
                    $scope.carregar();
                    $scope.produto = {};
                    $('form').find('input[type=submit]').val('Adicionar');
                }
                showMessage(r);
            }
        );
    };

    $scope.editarProduto = function(index, id) {
        $scope.produto = $scope.produtos[index];
        $('form').find('input[type=submit]').val('Editar produto');
    };

    $scope.removerProduto = function(index, id) {
        if (confirm("Tem certeza que deseja remover o produto #" + id + " da lista?")) {
            requests(
                $http,
                '/api/produto',
                'delete',
                {id: id},
                function (r) {
                    $scope.produtos.splice(index, 1);
                }
            );
        }
    };

    $scope.carregar();
});