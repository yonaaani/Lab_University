var app = angular.module('myApp', []);

    app.controller('myController', function($scope) {
      //1
      $scope.name = 'Петро';
      $scope.surname = 'Петренко';
      $scope.age = 25;

      //2
      $scope.langs = {
    name: 'Петро',
    surname: 'Петренко',
    age: '25'
  };

  //3
  $scope.languages = ['html', 'css', 'js', 'php'];
  $scope.countries = {
    "Варшава": "Польща",
    "Вільнюс": "Литва",
    "Київ": "Україна"
};

//4
 $scope.workers = [
    {name: 'Микола', age: 30, salary: 400},
    {name: 'Василь', age: 31, salary: 500},
    {name: 'Петро', age: 32, salary: 600},
    ];

  //5
  $scope.name = 'Іван';
  $scope.changeName = function() {
    $scope.name = 'Дмитро';
  };

  //6
  $scope.name6 = 'Іван';
      $scope.surname6 = 'Іванів';
      $scope.age6 = 25;

      $scope.changeName6 = function() {
        $scope.name6 = 'Петро';
      };

      $scope.changeSurname6 = function() {
        $scope.surname6 = 'Петренко';
      };

      $scope.changeAge6 = function() {
        $scope.age6 = 30;
      };

  //7
  $scope.languages7 = ['html', 'css', 'js', 'php'];

  $scope.changeLanguage7 = function() {
    var index = $scope.languages7.indexOf('php');
    if (index !== -1) {
      $scope.languages7[index] = 'sql';
    }
  };
  //8
  $scope.languages8 = ['html', 'css', 'js', 'php'];
  
    $scope.addLanguage8 = function() {
      $scope.languages8.push('sql');
    };

  //9
  $scope.languages9 = ['html', 'css', 'js', 'php'];

			$scope.addLanguage9 = function() {
				$scope.languages9.unshift('sql');
			};

  //10
  $scope.languages10 = ['html', 'css', 'js', 'php'];

			$scope.removeLanguage10 = function(lang) {
				var index = $scope.languages10.indexOf(lang);
				if (index > -1) {
					$scope.languages10.splice(index, 1);
				}
			};

  //11
  $scope.languages11 = ['html', 'css', 'js', 'php'];

      $scope.removeLanguage11 = function(language11) {
        var index = $scope.languages11.indexOf(language11);
        if (index !== -1) {
          $scope.languages11.splice(index, 1);
        }
      };

  //додала аби кожен раз при натисненні на href не повертало на початок сторінки
  $scope.scrollToTop = function(event) {
    event.preventDefault();
    window.scrollTo(0, 0);
  }

  $scope.userInfo = $scope.langs.name + ' ' + $scope.langs.surname + ', ' + $scope.langs.age + ' років';
});
    