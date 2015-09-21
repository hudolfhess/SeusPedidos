/**
 * Created by hcassus on 9/17/15.
 */
app.controller("clienteCtrl", function($scope, $http) {

    $scope.clientes = [];

    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

    $scope.carregar = function() {
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

    $scope.adicionaCliente  = function() {
        requests(
            $http,
            '/api/cliente',
            'post',
            $scope.cliente,
            function(r) {
                $('form .form-group').removeClass('has-error');
                if (r.data.success == 1) {
                    $scope.carregar();
                    $scope.cliente = {};
                    $('form').find('input[type=submit]').val('Adicionar');
                }
                showMessage(r);
            }
        );
    };

    $scope.editarCliente = function(index, id) {
        $scope.cliente = $scope.clientes[index];
        $('form').find('input[type=submit]').val('Editar cliente');
    };

    $scope.removerCliente = function(index, id, name) {
        if (confirm("Tem certeza que deseja remover o cliente " + name + " da lista?")) {
            requests(
                $http,
                '/api/cliente',
                'delete',
                {id: id},
                function (r) {
                    $scope.clientes.splice(index, 1);
                }
            );
        }
    }

    $scope.carregar();

});