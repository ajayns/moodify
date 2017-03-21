var app = angular.module('app', ['angularSoundManager']);

app.controller('appCtrl', function($scope) {
  $scope.songs = [
    {
      id: 'one',
      title: 'one',
      artist: 'one',
      url: 'http://www.schillmania.com/projects/soundmanager2/demo/_mp3/rain.mp3'
    },
    {
      id: 'two',
      title: 'two',
      artist: 'two',
      url: 'http://www.schillmania.com/projects/soundmanager2/demo/_mp3/walking.mp3'
    },
    {
      id: 'three',
      title: 'three',
      artist: 'three',
      url: 'http://www.freshly-ground.com/misc/music/carl-3-barlp.mp3'
    }
  ]
})
