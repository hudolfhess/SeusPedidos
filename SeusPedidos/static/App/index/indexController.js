app.controller("indexController", function($scope, $http) {
    $scope.doLogin = function() {
        requests(
            '/api/login',
            'post',
            '#login-form',
            function(r) {
                console.log(r)
            }
        );

        /*
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';

        var request = $http({
            method: "post",
            url: "/api/login",
            data: $.param({
                'username': document.getElementById("input-username").value,
                'password': document.getElementById("input-password").value,
            }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
        });
        request.success(
            function (html) {
                $scope.cfdump = html;
            }
        );
        */

    }
});