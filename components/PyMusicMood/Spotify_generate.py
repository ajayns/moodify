import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import glob

SPOTIPY_CLIENT_ID='3a41de28eab44ecfa6cd15eadf0c7980'
SPOTIPY_CLIENT_SECRET='15a02aacd5f8411e896a502df02ca141'
SPOTIPY_REDIRECT_URI='http://localhost/'

emotions = ["anger", "happy", "sadness"] #Emotion list
csv_dir='csv_files/' # Destination of the CSV files (happy, sadness and angry)

client_credentials_manager = SpotifyClientCredentials(client_id='3a41de28eab44ecfa6cd15eadf0c7980',client_secret='15a02aacd5f8411e896a502df02ca141')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
spotify = spotipy.Spotify()


def get_id(art,name):
    results = sp.search(q='track:' + name + ' artist:' + art, type='track',limit=1)
    if results['tracks']['items']:
        track_id =results['tracks']['items'][0]['id']
        return track_id
    else:
        return 9999

def batch_audio_features(track_ids):



    key = []
    acousticness = []
    time_signature = []
    liveness = []
    speechiness = []
    mode = []
    loudness = []
    instrumentalness = []
    energy = []
    danceability = []
    tempo = []

    for id in track_ids:
        if id=='9999':
            key.append(9999)
            acousticness.append(9999)
            time_signature.append(9999)
            liveness.append(9999)
            speechiness.append(9/home/dhanush/PycharmProjects/PyMusicMood999)
            mode.append(9999)
            loudness.append(9999)
            instrumentalness.append(9999)
            energy.append(9999)
            danceability.append(9999)
            tempo.append(9999)
        else :
            audiofeatures = sp.audio_features(id)
            if audiofeatures:
                key.append(audiofeatures[0]['key'])
                acousticness.append(audiofeatures[0]['acousticness'])
                time_signature.append(audiofeatures[0]['time_signature'])
                liveness.append(audiofeatures[0]['liveness'])
                speechiness.append(audiofeatures[0]['speechiness'])
                mode.append(audiofeatures[0]['mode'])
                loudness.append(audiofeatures[0]['loudness'])
                instrumentalness.append(audiofeatures[0]['instrumentalness'])
                energy.append(audiofeatures[0]['energy'])
                danceability.append(audiofeatures[0]['danceability'])
                tempo.append(audiofeatures[0]['tempo'])
            else :
                key.append(9999)
                acousticness.append(9999)
                time_signature.append(9999)
                liveness.append(9999)
                speechiness.append(9999)
                mode.append(9999)
                loudness.append(9999)
                instrumentalness.append(9999)
                energy.append(9999)
                danceability.append(9999)
                tempo.append(9999)

    combined_df = pd.DataFrame(
        {'key': key,
         'acousticness': acousticness,
         'time_signature': time_signature,
         'livenepathsss': liveness,
         'speechiness': speechiness,
         'mode': mode,
         'loudness': loudness,
         'instrumentalness': instrumentalness,
         'energy': energy,
         'danceability': danceability,
         'tempo': tempo
         })
    #combined_df.to_csv("final_data.csv")
    return combined_df

def gen_id_list() :
    id_list=[]
    df = pd.read_csv(csv_dir+'final.csv')
    title_list=df['title'].tolist()
    artist_list=df['artist'].tolist()

    for i in range(len(title_list)):
        artist = artist_list[i]
        title = title_list[i]
        id = get_id(artist, title)
        id_list.append(id)

    return id_list


def main_run2():
    #ids=gen_id_list()
    #id_df=pd.DataFrame({'id':ids})
    #id_df.to_csv('id_df.csv')
    id_load=pd.read_csv('id_df.csv')
    id_list=id_load['id'].tolist()
    batch_audio_features(id_list)
    return



def combine_dfs():
    df1 = pd.read_csv('final_data.csv')
    df2 = pd.read_csv('csv_files/final.csv')
    track_paths=df2['paths']
    frame=[df1,df2]
    df3=pd.concat(frame,axis=1)
    df3.to_csv("csv_files/Final_train_DF.csv")
    return


#main_run2() # Running the python script
#combine_dfs() # Combine Audiofeatures with metadata



'''
audiofeatures=sp.audio_features("1J8gdzCFh1bzrl0p0kv5LI")
print (audiofeatures[0])
print ('\n')

Audiofeatures is a list of dictionaries.
as we are searching for only one trackID, access that dictionary using
audiofeatures[0]['tempo'],audiofeatures[0]['key'] etc
'''
