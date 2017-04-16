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

// Get query variables and store mood
var getQuery = getQueryStrings();
var getMood = getQuery['mood'];

var app = angular.module('app', ['angularSoundManager', 'ngResource']);

// Resource service to GET songs
app.factory('Music', function($resource) {
  return $resource('music?mood=' + getMood);
});

app.controller('appCtrl', function($scope, Music) {
  // Save songs from DB
  $scope.songs = Music.query();

  // Init variables
  $scope.isPlaying = false;
  $scope.songHover = false;

})


