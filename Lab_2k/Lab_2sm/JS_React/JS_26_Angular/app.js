var app = angular.module('myApp', []);

    app.controller('myController', function($scope) {
      //1
      $scope.numbers = [1, 2, 3, 4, 5];
      //2
      $scope.numbers2 = [1, 2, 3, 4, 5];
      //3
      $scope.numbers3 = [1, 2, 3, 4, 5];

  $scope.reverseList3 = function() {
    $scope.numbers = $scope.numbers3.reverse();
  };

  //4
  $scope.numbers4 = [5, 2, 3, 1, 4];

  $scope.sortList4 = function() {
    $scope.numbers = $scope.numbers4.sort();
  };

  //5
  $scope.languages5 = ['html', 'css', 'js', 'php'];

  $scope.changeLanguage5 = function(index) {
    if ($scope.languages5[index].endsWith('+')) {
      $scope.languages5[index] = $scope.languages5[index].slice(0, -1);
    } else {
      $scope.languages5[index] += '+';
    }
  };

  //6
  $scope.users = ['Микола', 'Василь', 'Петро'];
    $scope.newUsers = ['Аня', 'Валя', 'Маша'];

    $scope.addUser = function() {
      if ($scope.newUsers.length > 0) {
        $scope.users.push($scope.newUsers.shift());
        $scope.users.sort();
      }
    };

  //7
  $scope.numbers7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

  //8
  $scope.workers = {
    Україна: ['Київ', 'Львів'],
    Польща: ['Варшава', 'Лодзь'],
    Великобританія: ['Лондон', 'Манчестер'],
  };

});
    