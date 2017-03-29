var app = angular.module('app', ['angularSoundManager']);

app.controller('appCtrl', function($scope) {
  $scope.songs = [
    {
      id: 'one',
      title: 'The First Track',
      artist: 'First Artist',
      album: 'One',
      url: 'http://www.schillmania.com/projects/soundmanager2/demo/_mp3/rain.mp3'
    },
    {
      id: 'two',
      title: 'The Second Track',
      artist: 'Second Artist',
      album: 'Two',
      url: 'http://www.schillmania.com/projects/soundmanager2/demo/_mp3/walking.mp3'
    },
    {
      id: 'three',
      title: 'The Third Track',
      artist: 'Third Artist',
      album: 'Three',
      url: 'http://www.freshly-ground.com/misc/music/carl-3-barlp.mp3'
    }
  ]

  $scope.isPlaying = false;
  $scope.songHover = false;
})
