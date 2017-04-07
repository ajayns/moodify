import pandas as pd
import glob
import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.utils import shuffle


svm_clf=SVC(kernel='linear',probability=True,tol=1e-3)


def pre_process():
    final_df = pd.read_csv('csv_files/Final_train_DF.csv')
    preprocess_df = final_df[final_df.key != 9999]
    preprocess_df.to_csv('csv_files/data_preprocess.csv')
    return

def get_train_data(rand_st):
    preprocess_df=pd.read_csv('csv_files/data_preprocess.csv')
    column_list=['acousticness','danceability','energy','instrumentalness','key','livenepathsss','loudness','speechiness','tempo']
    train_data=preprocess_df.as_matrix(column_list)
    train_labels=preprocess_df.as_matrix(['emotion'])
    t_d=shuffle(train_data, random_state=rand_st)
    t_l=shuffle(train_labels, random_state=rand_st)
    return t_d,t_l

def train_svm_model(rand_s=1):

    train_d,train_l=get_train_data(rand_s)
    svm_clf.fit(train_d[:int(len(train_d))], train_l[:int(len(train_l))])
    joblib.dump(svm_clf, 'trained_models/SVM_Music_model.pkl')
    #print("\nComputing Accuracy of : ")
    #final_pred = svm_clf.score(train_d[-int(len(train_d)*0.10):], train_l[-int(len(train_l)*0.10):])
    #print("\nAccuracy : %f" % final_pred)
    return

def test():
    pre_process()
    Acc_list=[]
    for i in range(1,30):
        accu=train_and_verify(i)
        Acc_list.append(accu)
    print("\n Mean Accuracy %f " %np.mean(Acc_list))
    return

train_svm_model()



