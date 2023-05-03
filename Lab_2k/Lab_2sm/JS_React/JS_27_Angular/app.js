var app = angular.module('myApp', []);

    app.controller('myController', function($scope) {
      //1
      $scope.number = 0;
      //2
      $scope.number2 = null;
      $scope.$watch('number2', function(newValue, oldValue) {
        $scope.square2 = newValue * newValue;
      });
      //3
      $scope.countries = ['Ukraine', 'USA', 'Canada', 'France'];
			$scope.addCountry = function() {
				$scope.countries.push($scope.newCountry);
				$scope.newCountry = "";
			};
      //4
      $scope.isChecked = false;
      //5
      $scope.isChecked5 = false;
      //6
      $scope.isChecked1 = false;
			$scope.isChecked2 = false;
      //7
      $scope.courses = {
        'html': true,
        'css': true,
        'php': false,
        'js': true,
        'angular': false
      };
});
    