function getQueryStrings() {
  var assoc  = {};
  var decode = function (s) { return decodeURIComponent(s.replace(/\+/g, " ")); };
  var queryString = location.search.substring(1);
  var keyValues = queryString.split('&');

  for(var i in keyValues) {
    var key = keyValues[i].split('=');
    if (key.length > 1) {
      assoc[decode(key[0])] = decode(key[1]);
    }
  }

  return assoc;
}

var getQuery = getQueryStrings();
var getMood = getQuery['mood'];

var app = angular.module('app', ['angularSoundManager', 'ngResource']);

app.factory('Music', function($resource) {
  return $resource('music?mood=' + getMood);
});

app.controller('appCtrl', function($scope, Music) {
  $scope.songs = Music.query();
  $scope.isPlaying = false;
  $scope.songHover = false;
})


