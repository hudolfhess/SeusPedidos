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
        requests(
            $http,
            '/api/produto',
            'post',
            $scope.produto,
            function(r) {
                $('form .form-group').removeClass('has-error');
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

    $scope.removerProduto = function(index, id, name) {
        if (confirm("Tem certeza que deseja remover o produto " + name + " da lista?")) {
            requests(
                $http,
                '/api/produto',
                'delete',
                {id: id},
                function (r) {
                    if (r.data.success == 1) {
                        $scope.produtos.splice(index, 1);
                    } else {
                        alert("Não foi possível remover o produto pois ele já está relacionado com um pedido.")
                    }
                }
            );
        }
    };

    $scope.carregar();
});