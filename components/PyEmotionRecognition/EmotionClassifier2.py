import cv2
import numpy as np
import dlib
from sklearn.svm import SVC
import glob
import random
import math
from sklearn.externals import joblib

emotions = ["anger", "happy", "sadness"] #Emotion list
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)) # Histogram equalization object
face_det=dlib.get_frontal_face_detector()
land_pred=dlib.shape_predictor("data/DlibPredictor/shape_predictor_68_face_landmarks.dat")

svm_clf2=SVC(kernel='linear',probability=True,tol=1e-3) # SVM classifier object

def get_images(emotion):
    m_path='INCLUDE THE MAIN PATH TO YOUR IMAGES AFTER RUNNING ORGANIZE DATA'
    i_path=glob.glob(m_path+emotion+'/*')
    # print(i_path)
    random.shuffle(i_path) # Shuffle the list of image paths
    train_paths=i_path[:int(len(i_path)*0.90)] # For validation, 90 percent of training data is used
    predict_paths=i_path[-int(len(i_path)*0.10):] # and 10 percent as test data.
    return train_paths,predict_paths

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

        if x_cords[26]==x_cords[29]: # 26 is the top of the bridge, 29 is the tip of the nose
            anglenose=0
        else:
            anglenose_rad=int(math.atan((y_central[26] - y_central[29]) / (x_central[26] - x_central[29])))
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
            np_mean_coor=np.asarray((ymean,xmean))
            np_coor=np.asarray((z,w))
            euclid_d=np.linalg.norm(np_coor-np_mean_coor)
            landmarks_v.append(euclid_d)

            # Angle of the vector, which is used to correct for the offset caused due to tilt of image wrt horizontal
            angle_rad = (math.atan((z - ymean) / (w - xmean)))
            angle_degree = math.degrees(angle_rad)
            angle_req = int(angle_degree - anglenose)
            landmarks_v.append(angle_req)

    if len(face_detections)<1:
        landmarks_v="error"

    return  landmarks_v

def org_data():
    train_data=[]
    train_labels=[]
    pred_data=[]
    pred_labels=[]

    for emo in emotions:
        train_p,pred_p=get_images(emo)
        for im in train_p:
            img=cv2.imread(im)
            img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            clahe_gray=clahe.apply(img_gray)
            landmarks_vec=get_landmarks(clahe_gray)
            if landmarks_vec == "error":
                pass
            else:
                train_data.append(landmarks_vec)
                train_labels.append(emotions.index(emo))

        for im in pred_p:
            img=cv2.imread(im)
            img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            clahe_gray=clahe.apply(img_gray)
            landmarks_vec=get_landmarks(clahe_gray)
            if landmarks_vec == "error":
                pass
            else:
                pred_data.append(landmarks_vec)
                pred_labels.append(emotions.index(emo))

    return train_data,train_labels,pred_data,pred_labels

accuracy=[]

for i in range(0,10):
    print("\nSetting Random sample sets %d " %i)
    train_data, train_labels, pred_data, pred_labels=org_data()

    np_train_data=np.array(train_data)
    np_train_labels=np.array(train_labels)
    print(np_train_data)
    print("\nTraining SVM model with Linear Kernel : %d " %i)
    svm_clf2.fit(np_train_data,np_train_labels)

    print("\nComputing Accuracy of : %d " %i)
    np_test_data=np.array(pred_data)
    final_pred=svm_clf2.score(np_test_data,pred_labels)
    print("\nAccuracy : %f" %final_pred)
    accuracy.append(final_pred)
joblib.dump(svm_clf2,'data/Trained_ML_Models/SVM_new_model.pkl') # MODIFY THE NAME OF THE MODEL TO BE SAVED.
print("\n Mean Accuracy %f " %np.mean(accuracy))






