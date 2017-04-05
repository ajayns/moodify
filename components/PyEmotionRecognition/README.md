# PyEmotionRecognition
A Python project to detect an individual's face and recognize emotions expressed, given an image.

## Getting Started
### Prerequisites
The following Python 3 libraries are to be installed (If not already installed) :
1) OpenCV
2) numpy
3) dlib
4) scikit-Learn
5) random
6) glob
7) math
8) itertools

Most of the above mentioned libraries can be installed using 
```
sudo pip3 install <library-name>
```

For installing OpenCV on Ubuntu 16.04, use the link : 
http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/

Download the dlib predictor that has been used in the project from : 
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
and move it to the location in the project 'data/DlibPredictor'

The CK+ dataset has been used for training this model, link : http://www.consortium.ri.cmu.edu/ckagree/

### Synopsis
A short description for the use of each python script :
1) OrganizeData.py       : Organizes the images present in the CK+ dataset into their respective emotion folders according to the                            emotion labels.
2) DataPreProcess.py     : Uses HAAR Cascades to detect faces and crop the organized images.
3) EmotionClassifier2.py : Trains and saves a Support Vector Machine classifier with linear kernel to classify future images                                according to emotion.
4) Model_test2.py        : Loads the saved SVM model, detects the face in the given image and predicts the emotion expressed.

