var app = angular.module('app', []);

app.controller('appCtrl', function($scope) {
  $scope.cam = true;

  $scope.snap = function() {
    $scope.cam = false;
  }

  $scope.retake = function() {
    $scope.cam = true;
  }
})
