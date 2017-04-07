from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import glob
import pandas as pd
import random
from mutagen.easyid3 import EasyID3
import pandas as pd




def get_song_paths(emotion):  # Function to return the path of all songs belonging to 'emotion'
    m_path='/home/dhanush/Music/MusicClassify/'
    i_path=glob.glob(m_path+emotion+'/*')
    print(i_path)
    return i_path
csv_dest='csv_files/' # Destination of the CSV files (happy, sadness and angry)_path

def get_batch_metadeta(paths):  # Function to get the metadata of a batch of mp3 files in the locations - paths
    titles=[]
    artists=[]
    for path in paths:
        audio = EasyID3(path)
        audio_title=audio['title']
        audio_artist=audio['artist']
        titles.append(audio_title)
        artists.append(audio_artist)
    return titles,artists,paths

def get_single_metadata(path):  # Function to get metadata of a single file at - path
    audio = EasyID3(path)
    audio_title = audio['title']
    audio_artist = audio['artist']
    return audio_title,audio_artist

def conv_to_dataframe(titles,artists,emot,paths,ind_beg):
    combined_df = pd.DataFrame(
        {'title': titles,
         'artist': artists,
         'paths':paths
         },)

    combined_df['emotion'] = emot
    return combined_df.index(emo)

def main_run():
    emotions = ["anger", "happy", "sadness"]  # Emotion list
    csv_dest = 'csv_files/'  # Destination of the CSV files (happy, sadness and angry)
    ind=0
    for emo in emotions:
        paths = get_song_paths(emo)
        ind=ind+(len(paths)-1)
        titles,artists,_ = get_batch_metadeta(paths)
        final_df=conv_to_dataframe(titles, artists, emotions.index(emo)+1, paths,ind)
        final_df.to_csv(csv_dest+emo+'.csv')

    happy=pd.read_csv(csv_dest+'happy.csv')
    happy=happy[['title','artist','paths','emotion']]
    sadness = pd.read_csv(csv_dest + 'sadness.csv')
    sadness = sadness[['title', 'artist', 'paths', 'emotion']]
    anger = pd.read_csv(csv_dest + 'anger.csv')
    anger = anger[['title', 'artist', 'paths', 'emotion']]
    frames = [happy, sadness, anger]
    final_conc=pd.concat(frames)
    final_conc.to_csv(csv_dest+"final.csv")
# RUNNING THE SCRIPT

#main_run()





