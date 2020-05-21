# Moodify

***(Not longer maintained)***

A WebApp which uses a snapshot taken of the user to detect emotion and using this, generate a suitable music playlist. This project was built for ACM Month Of Code, actual coding done in about 3 weeks.

Read the detailed article on building Moodify here: https://medium.com/@ajay.ns08/acm-month-of-code-2k17-building-moodify-d5d9e0c52ca7

## Implementation
The Cam, Music Player, scripts for emotion recognition and Database were wired and wrapped up into a WebApp using Flask, using routes to use the Backend like an API while the frontend handles the user.

Being an experimental setup built in such a short span of time, the user interface and flow would require multiple fixes before deployment.


## Installation
You should have the following preinstalled:
* OpenCV
* MongoDB
* [dlib Predictor](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 ) data files to be placed in data/
* Haar Cascades data files to be placed in data/
* Python 2 
* files/mp3 and files/img store the music data and album art

Preferably setup a Virtual Env and then you'll just need to install packages:

```bash
pip install -r requirements.txt
```

Make sure you have MongoDB running to host the database. Also run a simple http server to serve the files/ folder at localhost:8000

```bash
cd files
python -m SimpleHTTPServer
```


Start the program
```bash
python app.py
```

Open the webapp from browser at localhost:5000


## Technologies
### Frontend
* [AngularJS](https://angularjs.org/) : JavaScript framework for programming the music player.
* [Materialize](http://materializecss.com/) : CSS Framework for skinning the app based on Google's Material Design.
* [WebcamJS](https://github.com/jhuckaby/webcamjs) : JavaScript library for Image Capture
* [Angular SoundManager 2](https://github.com/perminder-klair/angular-soundmanager2) : Adds music player functionality for AngularJS using SoundManager 2 API

### Backend
 * [Flask](http://flask.pocoo.org/) : A microframework for Python for Web App building
 * [OpenCV](http://opencv.org/) : Open source Computer Vision, used here for facial recognition, analysis and emotion identification.
 * A few machine learning libraries used along with OpenCV such as dlib, NumPy, scikit

## Individual Components
* [ng-musicplayer](https://github.com/ajayns/ng-musicplayer) : The music player component built on AngularJS and Materialize.
* [PyEmotionRecognition](https://github.com/dhanushkamath/PyEmotionRecognition) : The script used to detect the mood from an image using OpenCV and machine learning libraries.
* [PyMusicMood](https://github.com/dhanushkamath/PyMusicMood) : For automatic classification of music into moods based on parameters extracted from Spotify API. 
* Cam-App, Py-Flask-Wa : Initial code in setting up the Cam and Flask Server
