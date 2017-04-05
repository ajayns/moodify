import glob
from shutil import copyfile

emotions = ["neutral","anger","contempt","disgust","fear","happy","sadness","surprise"]
candidates_paths=glob.glob("<INCLUDE THE PATH OF THE CK+ DATASET>")

for x in candidates_paths:
    serial=x[-4:]
    for sessions in glob.glob("data/FaceData/Emotion/%s/*" %serial):
        for files in glob.glob("%s/*" %sessions):
            file=open(files,'r')
            current_session=files[46:-30]
            current_emotion=int(float(file.readline()))

            a=glob.glob("data/FaceData/Images/%s/%s/*" %(serial, current_session))
            b=sorted(a)
            image_emotion_s=b[-1]
            image_neutral_s=b[0]

            neutral_d="data/FaceData/OrganizedData/neutral/%s" %image_neutral_s[50:]
            emo_d = "data/FaceData/OrganizedData/%s/%s" %(emotions[current_emotion],image_neutral_s[50:])

            copyfile(image_neutral_s,neutral_d)
            copyfile(image_emotion_s,emo_d)



