import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import glob
import Spotify_generate as sg
import lib_csv_generator as lib_csv
from sklearn.externals import joblib
from sklearn.svm import SVC

def gen_id_df(lib_path):
    emotions = ["anger", "happy", "sadness"]

    music_paths = glob.glob(lib_path+'*.mp3')
    title_list,artist_list,paths = lib_csv.get_batch_metadeta(music_paths)

    id_list = []

    for i in range(len(title_list)):
        artist = artist_list[i]
        title = title_list[i]
        id = sg.get_id(artist[0], title[0])
        id_list.append(id)

    init_df = pd.DataFrame(
        {'title': title_list,
         'artist': artist_list,
         'paths': paths,
         'id':id_list
         }, )

    return init_df



def pred_emotion(result):
    column_list = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'livenepathsss', 'loudness',
                   'speechiness', 'tempo']
    test_data = result.as_matrix(column_list)
    emotions = ["anger", "happy", "sadness"]
    svm_clf = joblib.load('trained_models/SVM_Music_model.pkl')
    emot_i=svm_clf.predict(test_data)
    emo=[]
    for i in emot_i:
        emo.append(emotions[i])

    emo_df=pd.DataFrame({'emotion':emo},)
    return emo_df

def main_func2():
    lib_path = '/home/dhanush/Music/TestClass/'
    id_df=gen_id_df(lib_path)
    audio_f_df=sg.batch_audio_features(id_df['id'].tolist())
    audio_test = pd.concat([id_df, audio_f_df], axis=1)
    audio_test.to_csv('test_data/test.csv')
    emo=pred_emotion(audio_test)
    audio_result=pd.DataFrame({'title':audio_test['title'].tolist(),
                               'artist':audio_test['artist'].tolist(),
                               'path':audio_test['path'].tolist(),
                               'emotion':emo},)

    audio_result.to_csv('test_data/result.csv')

main_func2()





