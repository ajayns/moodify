# ACM Month of Code Project

A WebApp which uses a snapshot taken of the user to detect emotion and using this, generate a suitable music playlist.


## Installation
You should have the following preinstalled:
* OpenCV
* MongoDB

Preferably setup a Virtual Env and then you'll just need to install packages:

```bash
pip install -r requirements.txt
```

Make sure you have MongoDB running to host the database. Also run a simple http server to serve the files folder at localhost:8000

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
