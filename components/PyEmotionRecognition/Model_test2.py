
# EMOTION RECOGNITION PYTHON SCRIPT.

import cv2
import numpy as np
import dlib
from sklearn.svm import SVC
import glob
import random
import math
import itertools
from sklearn.externals import joblib



img_path='data/test_images/test1.jpg' # THE PATH OF THE IMAGE TO BE ANALYZED

font=cv2.FONT_HERSHEY_DUPLEX
emotions = ["anger", "happy", "sadness"] #Emotion list
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)) # Histogram equalization object
face_det=dlib.get_frontal_face_detector()
land_pred=dlib.shape_predictor("data/DlibPredictor/shape_predictor_68_face_landmarks.dat")







def crop_face(i_path):

    image=cv2.imread(i_path)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    dest_i = 'data/cap_image/test.png'
    # Loading all the HAAR Cascade classifiers
    face1 = cv2.CascadeClassifier("data/HAARCascades/haarcascade_frontalface_default.xml")
    face2 = cv2.CascadeClassifier("data/HAARCascades/haarcascade_frontalface_alt2.xml")
    face3 = cv2.CascadeClassifier("data/HAARCascades/haarcascade_frontalface_alt.xml")
    face4 = cv2.CascadeClassifier("data/HAARCascades/haarcascade_frontalface_alt_tree.xml")

    # Detecting faces
    face_1 = face1.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5),flags=cv2.CASCADE_SCALE_IMAGE)
    face_2 = face2.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5),flags=cv2.CASCADE_SCALE_IMAGE)
    face_3 = face3.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5),flags=cv2.CASCADE_SCALE_IMAGE)
    face_4 = face4.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)

    # ensuring that no other object in the image has been wrongly classified as a face and at least one face is
    # detected.
    if len(face_1)==1:
        req_face=face_1
    elif len(face_2) == 1:
        req_face = face_2
    elif len(face_3) == 1:
        req_face = face_3
    elif len(face_4) == 1:
        req_face = face_4
    else:
        req_face=""
    if len(req_face)==1:
        print("\n Face Cropped Using HAAR Cascade\n")
        for (x, y, w, h) in req_face:
            roi_gray = gray[y:y + h, x:x + w]
        # Writing the final cropped image to the required directory

        cv2.imwrite(dest_i, cv2.resize(roi_gray, (350, 350)))
    else:
        print("\n Face Not Cropped Using HAAR Cascade\n")

        cv2.imwrite(dest_i,gray)
    return dest_i


def get_landmarks(image_p):
    face_detections=face_det(image_p,1)
    for k,d in enumerate(face_detections):
        shape=land_pred(image_p,d)
        x_cords=[]
        y_cords=[]
        for i in range(1,68):
            x_cords.append(float(shape.part(i).x))
            y_cords.append(float(shape.part(i).y))

        xmean=np.mean(x_cords)
        ymean=np.mean(y_cords)
        x_central=[(x-xmean) for x in x_cords] # To compensate for variation in location of face in the frame.
        y_central=[(y-ymean) for y in y_cords]

        if x_cords[26]==x_cords[29]: # 26 is the top of the top of the  nose-bridge, 29 is the tip of the nose
            anglenose=0
        else:
            anglenose_rad=int(math.atan((y_central[26]-y_central[29])/(x_central[26]-x_central[29])))
            # Tan Inverse of slope
            anglenose=int(math.degrees(anglenose_rad))
            # print(y_central[26]-y_central[29])
            # print(y_cords[26]-y_cords[29])

        if anglenose<0:
            anglenose+=90 # Because anglenose computed above is the angle wrt to vertical

        else:
            anglenose-=90      # Because anglenose computed above is the angle wrt to vertical

        landmarks_v=[]
        for x,y,w,z in zip(x_central,y_central,x_cords,y_cords):
            landmarks_v.append(x) # Co-ordinates are added relative to the Centre of gravity of face to accompany for
            landmarks_v.append(y) # variation of location of face in the image.

            # Euclidean distance between each point and the centre point (length of vector)
            np_mean_co=np.asarray((ymean,xmean))
            np_coor=np.asarray((z,w))
            euclid_d=np.linalg.norm(np_coor-np_mean_co)
            landmarks_v.append(euclid_d)

            # Angle of the vector(used to compensate for the offset caused due to tilt of face wrt horizontal)
            angle_rad=(math.atan((z-ymean)/(w-xmean)))
            angle_degree=math.degrees(angle_rad)
            angle_req=int(angle_degree-anglenose)
            landmarks_v.append(angle_req)

    if len(face_detections)<1:
        landmarks_v="error"

    return  landmarks_v

# Loading the Support Vector Machine model from storage after training
# with linear kernel in EmotionClassifer2.py
# SVM_emo_model_4.pkl has been trained with the cropped face dataset(using HAAR cascades)
# SVM_emo_model_5.pkl has been trained with Original Organized Dataset
# SVM_emo_model_4.pkl is giving better results on new data.
# SVM_emo_model_7.pkl is giving the best accuracy.


SUPPORT_VECTOR_MACHINE_clf2 = joblib.load('data/Trained_ML_Models/SVM_emo_model_7.pkl')
# Loading the SVM model trained earlier in the path mentioned above.



pred_data=[]
pred_labels=[]

a=crop_face(img_path)
img=cv2.imread(a)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
clahe_gray=clahe.apply(gray)
landmarks_vec = get_landmarks(clahe_gray)

print(len(landmarks_vec))
print(landmarks_vec)

if landmarks_vec == "error":
    pass
else:
    pred_data.append(landmarks_vec)
np_test_data = np.array(pred_data)
a=SUPPORT_VECTOR_MACHINE_clf2.predict(pred_data)
cv2.putText(img,'DETECTED FACIAL EXPRESSION : ',(8,30),font,0.7,(0,0,255),2,cv2.LINE_AA)
l=len('Facial Expression Detected : ')
cv2.putText(img,emotions[a[0]].upper(),(150,60),font,1,(255,0,0),2,cv2.LINE_AA)
cv2.imshow('test_image',img)
print(emotions[a[0]])


cv2.waitKey(0)
cv2.destroyAllWindows()
