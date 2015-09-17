/**
 * Created by hcassus on 9/17/15.
 */
app.controller("produtoCtrl", function($scope) {

    $scope.produtos = [];

    requests(
        '/api/produto',
        'get',
        null,
        function(r) {
            console.log(r)
        }
    )

    $scope.adicionaProduto  = function() {
        requests(
            '/api/produto',
            'post',
            $scope.produto,
            function(r) {
                console.log(r)
            }
        );

        /*
        produto = $scope.produto;
        $scope.produtos.push(produto);
        $scope.produto = {};
        */
    };

    $scope.removerProduto = function(index) {
        $scope.produtos.splice(index,1);
    }



});