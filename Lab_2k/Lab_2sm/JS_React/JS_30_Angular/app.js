var app = angular.module('myApp', []);

    app.controller('myController', function($scope) {
      //1
      $scope.users = [
        {id: 1, name: 'John Doe', email: 'johndoe@example.com'},
        {id: 2, name: 'Jane Smith', email: 'janesmith@example.com'},
        {id: 3, name: 'Bob Johnson', email: 'bobjohnson@example.com'}
      ];
    
      // Функція для перетворення імен користувачів у верхній регістр
      $scope.toUpper = function(str) {
        return str.toUpperCase();
      };

      //3
      $scope.users3 = [
        { name: 'John Doe', dob: '1990-05-20' },
        { name: 'Jane Smith', dob: '1985-11-12' },
        { name: 'Bob Johnson', dob: '1978-03-08' }
      ];
      
      $scope.formatDate = function(dateString) {
        var date = new Date(dateString);
        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();
        return day + '.' + month + '.' + year;
      };

      //4
      $scope.users4 = [
        {name: 'John', age: 25, dateOfBirth: '1998-04-12'},
        {name: 'Alice', age: 32, dateOfBirth: '1991-12-04'},
        {name: 'Bob', age: 18, dateOfBirth: '2005-09-01'}
      ];

      $scope.users4.sort(function(a, b) {
        return a.age - b.age;
      });

      //5
      $scope.users8 = [
        { name: 'John', age: 25 },
        { name: 'Mary', age: 30 },
        { name: 'Bob', age: 20 },
        { name: 'Alice', age: 27 },
        { name: 'Tom', age: 22 }
      ];

      //12
      $scope.users12 = [
        { name: 'John Doe', email: 'johndoe@example.com' },
        { name: 'Jane Doe', email: 'janedoe@example.com' },
        { name: 'Bob Smith', email: 'bobsmith@example.com' }
      ];
    
      $scope.filterUsers = function() {
        var query = $scope.searchQuery.toLowerCase();
        $scope.filteredUsers = [];
    
        angular.forEach($scope.users12, function(user) {
          if (user.name.toLowerCase().indexOf(query) !== -1) {
            $scope.filteredUsers.push(user);
          }
        });
      };
    
});
    