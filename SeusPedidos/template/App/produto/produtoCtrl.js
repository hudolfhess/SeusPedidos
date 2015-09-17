/**
 * Created by hcassus on 9/17/15.
 */
app.controller("produtoCtrl", function($scope) {

    $scope.produtos = [
        {nome:'Cogumelo Verde', valor:50.00},
        {nome:'Flor', valor:60.00},
        {nome:'Estrela', valor:80.00},
        {nome:'Cogumelo Vermelho', valor:40.00}
    ];

    $scope.adicionaProduto  = function() {
        produto = $scope.produto;
        $scope.produtos.push(produto);
        $scope.produto = {};
    };

    $scope.removerProduto = function(index) {
        $scope.produtos.splice(index,1);
    }



});