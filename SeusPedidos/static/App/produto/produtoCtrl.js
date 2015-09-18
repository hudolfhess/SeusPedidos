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

    $scope.adicionaProduto  = function() {
        requests(
            $http,
            '/api/produto',
            'post',
            $scope.produto,
            function(r) {
                $scope.carregar();
                $scope.produto = {};
            }
        );
    };

    $scope.removerProduto = function(index, id) {
        console.log(id);
        $scope.produtos.splice(index,1);
    };

    $scope.carregar();
});