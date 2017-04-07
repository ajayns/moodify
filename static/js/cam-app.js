var app = angular.module('app', []);

app.controller('appCtrl', function($scope) {
  $scope.cam = true;

  $scope.snap = function() {
    $scope.cam = false;
    Webcam.snap(function(data_uri) {
      $scope.imgURI = data_uri;
      document.getElementById('imgIn').value = data_uri;
    });
  }

  $scope.retake = function() {
    $scope.cam = true;
  }
});

Webcam.set({
      width: 640,
      height: 480,
      image_format: 'jpeg',
      jpeg_quality: 90
});

Webcam.attach('#cam');

