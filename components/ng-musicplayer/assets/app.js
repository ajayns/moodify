var app = angular.module('app', ['angularSoundManager']);

app.controller('appCtrl', function ($scope) {

  // Sample Data
  $scope.songs = [
    { id: "1",
      mood: "happy",
      title: "Take My Breath Away",
      artist: "Alesso",
      url: "src/mp3/1.mp3",
      albumart: "src/img/1.jpg",
      album: "Singles"
    },
    { id: "2",
      mood: "happy",
      title: "Sleepwalker",
      artist: "Illenium",
      url: "src/mp3/2.mp3",
      albumart: "src/img/2.jpg",
      album: "Ashes"
    },
    { id: "3",
      mood: "happy",
      title: "Sweet Child O' Mine",
      artist: "Guns N' Roses",
      url: "src/mp3/3.mp3",
      albumart: "src/img/3.jpeg",
      album: "Singles"
    }
  ];

  // Init variables
  $scope.isPlaying = false;
  $scope.songHover = false;
})
