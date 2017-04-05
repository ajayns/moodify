import glob
import cv2

emotions={1:'happy',2:'sadness',3:'anger'}
# ONLY THREE EMOTIONS HAVE BEEN USED. SO COPY FOLDERS NAMED 'HAPPY', 'SADNESS' AND 'ANGRY' AFTER USING OrganizeData.py
# to the folder OrganizedData2, MANUALLY.

m_dir='data/FaceData/OrganizedData2/'
dest_m_dir='data/FaceData/Crop_Organized_Data4/'

def crop_face(i_path,e_path):

    image=cv2.imread(i_path)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

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

    for (x, y, w, h) in req_face:
        roi_gray = gray[y:y + h, x:x + w]
    # Writing the final cropped image to the required directory
    temp_1=i_path
    temp_split=temp_1.split('/')
    final_name=temp_split[len(temp_split)-1]
    cv2.imwrite(dest_m_dir+e_path[48:]+'/'+final_name, cv2.resize(roi_gray, (350, 350)))


for emo_path in glob.glob(m_dir + '*'):
    for image_path in glob.glob(emo_path+'/*'):
        print (image_path)
        crop_face(image_path,emo_path)




