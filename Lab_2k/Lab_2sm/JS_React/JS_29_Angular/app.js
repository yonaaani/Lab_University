var app = angular.module('myApp', []);

    app.controller('myController', function($scope) {
      //1
      $scope.showParagraph = false;
      //2
      $scope.showParagraph2 = true;
      //3
      $scope.isParagraphVisible3 = true;

  $scope.hideParagraph3 = function() {
    $scope.isParagraphVisible3 = false;
  };

  $scope.showParagraph3 = function() {
    $scope.isParagraphVisible3 = true;
  };

  //4
  $scope.isParagraphVisible4 = false;

  $scope.toggleParagraph4 = function() {
    $scope.isParagraphVisible4 = !$scope.isParagraphVisible4;
  };

  //5
  $scope.showParagraph14 = false;
  $scope.showParagraph24 = false;
  $scope.showParagraph34 = false;

  //8
  $scope.countries = ['Україна', 'США', 'Канада', 'Іспанія', 'Італія', 'Німеччина', 'Франція'];
  $scope.selectedCountry = $scope.countries[0]; // за замовчуванням вибрана перша країна з масиву

  //9
  $scope.cities = [
    { name: 'New York' },
    { name: 'London' },
    { name: 'Paris' },
    { name: 'Tokyo' },
  ];
  $scope.selectedCity = $scope.cities[0];
  $scope.$watch('selectedCity', function(newValue, oldValue) {
    if (newValue !== oldValue) {
      $scope.selectedCity.name = newValue.name;
    }
  });

  //10
  $scope.countries1 = [
    {
      name: "Україна",
      cities1: [
        { name: "Київ" },
        { name: "Львів" },
        { name: "Харків" }
      ]
    },
    {
      name: "США",
      cities1: [
        { name: "Нью-Йорк" },
        { name: "Чикаго" },
        { name: "Лос-Анджелес" }
      ]
    },
    {
      name: "Велика Британія",
      cities1: [
        { name: "Лондон" },
        { name: "Манчестер" },
        { name: "Ліверпуль" }
      ]
    }
  ];
    
});
    