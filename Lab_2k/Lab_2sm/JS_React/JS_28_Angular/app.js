var app = angular.module('myApp', []);

    app.controller('myController', function($scope) {
      //1
      $scope.countries = [
        { name: 'Україна' },
        { name: 'США' },
        { name: 'Канада' },
        { name: 'Франція' },
        { name: 'Іспанія' }
      ];
    
      $scope.addCountry = function() {
        if ($scope.newCountry) {
          $scope.countries.push({ name: $scope.newCountry });
          $scope.newCountry = '';
        }
      };
    
      $scope.deleteCountry = function() {
        if ($scope.deleteIndex && $scope.deleteIndex > 0 && $scope.deleteIndex <= $scope.countries.length) {
          $scope.countries.splice($scope.deleteIndex - 1, 1);
          $scope.deleteIndex = '';
        }
      };

      //2
      $scope.countries2 = [
        { name: 'Україна' },
        { name: 'США' },
        { name: 'Канада' },
        { name: 'Франція' },
        { name: 'Іспанія' }
      ];
    
      $scope.addCountry2 = function() {
        if ($scope.newCountry2) {
          $scope.countries2.push({ name: $scope.newCountry2.trim().toLowerCase() });
          $scope.newCountry2 = '';
        }
      };
    
      $scope.removeCountry2 = function() {
        if ($scope.deleteCountry2) {
          var index = -1;
          for (var i = 0; i < $scope.countries2.length; i++) {
            if ($scope.countries2[i].name.trim().toLowerCase() === $scope.deleteCountry2.trim().toLowerCase()) {
              index = i;
              break;
            }
          }
          if (index !== -1) {
            $scope.countries2.splice(index, 1);
            $scope.deleteCountry2 = '';
          }
        }
      };
      
      //3
      $scope.countries3 = [
        'Україна',
        'США',
        'Канада',
        'Франція',
        'Іспанія',
        'Португалія'
      ];
    
      $scope.filterCountries = function(country3) {
        if ($scope.onlyShowCountriesWithP) {
          return country3.toLowerCase().indexOf('п') !== -1;
        } else {
          return true;
        }
      };

      //4
      $scope.options = [
        {label: 'Опція 1', selected: false},
        {label: 'Опція 2', selected: false},
        {label: 'Опція 3', selected: false},
        {label: 'Опція 4', selected: false},
        {label: 'Опція 5', selected: false},
      ];
    
      $scope.updateCheckboxes = function() {
        var numbers = $scope.checkboxNumbers.split(',');
        for (var i = 0; i < $scope.options.length; i++) {
          $scope.options[i].selected = false;
          for (var j = 0; j < numbers.length; j++) {
            if (numbers[j] === (i + 1).toString()) {
              $scope.options[i].selected = true;
              break;
            }
          }
        }
      };

      //5
      $scope.users = ['Микола', 'Василь', 'Петро'];
  $scope.newUsers = ['Іван', 'Дмитро', 'Андрій'];

  $scope.addUsers = function() {
    for (var i = 0; i < $scope.newUsers.length; i++) {
      $scope.users.push($scope.newUsers[i]);
    }
    $scope.newUsers = [];
  };

  //6
  $scope.numbers = [1, 2, 3, 4, 5];
        $scope.sum = calculateSum($scope.numbers);

        $scope.addNumber = function() {
          $scope.numbers.push(parseInt($scope.newNumber));
          $scope.sum = calculateSum($scope.numbers);
          $scope.newNumber = '';
        };

        function calculateSum(numbers) {
          return numbers.reduce(function(sum, number) {
            return sum + number;
          }, 0);
        };
    
});
    