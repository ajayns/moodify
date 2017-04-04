var app = angular.module('app', ['angularSoundManager', 'ngResource']);

app.factory('Music', function($resource) {
  return $resource('music/:id');
});

app.controller('appCtrl', function($scope, Music) {
  $scope.songs = Music.query();
  $scope.isPlaying = false;
  $scope.songHover = false;
})
