import pandas as pd
import matplotlib.pyplot as plt
import calendar
#from unidecode import unidecode


#Cleaning dataset process
top_tracks_2023 = pd.read_csv('Cleaned data/top_tracks_2023_cleaned.csv')
top_tracks_2023['track'] = top_tracks_2023['track'].str.split(' - ').str[0]
top_tracks_2023['track'] = top_tracks_2023['track'].str.split(':').str[0]

top_tracks_2023['track'] = top_tracks_2023['track'].str.replace(r'\s+\([^()]*\)$', '', regex=True)
top_tracks_2023['track'] = top_tracks_2023['track'].str.replace(r'\s+\([^()]*\)$', '', regex=True)
top_tracks_2023.loc[17, 'track'] = 'What Was I Made For?'
top_tracks_2023.loc[21, 'track'] = 'I Can See You'
top_tracks_2023.loc[36, 'track'] = 'Frágil'
top_tracks_2023.loc[44, 'track'] = 'Barbie World'
top_tracks_2023.loc[60, 'track'] = 'Tá OK'
top_tracks_2023.loc[79, 'track'] = 'CORAZÓN VACÍO'
top_tracks_2023.loc[82, 'track'] = 'Novidade na Área'
top_tracks_2023.loc[93, 'track'] = "Don't Blame Me"
top_tracks_2023.loc[26, 'artists'] = 'Rema, Selena G'

top_tracks_2023['track'] = top_tracks_2023['track'].apply(lambda x: x.title() \
                                                         if x[0] == x[0].lower()\
                                                         else x)

top_tracks_2023.to_csv('Cleaned data/top_tracks_2023_cleaned.csv', index=False)

#top_tracks_2022['track'] = top_tracks_2022['track'].str.split(' - ').str[0]
#top_tracks_2022['track'] = top_tracks_2022['track'].str.replace(r'\s+\([^()]*\)$', '', regex=True)
#top_tracks_2022['track'] = top_tracks_2022['track'].apply(lambda x: x.title() \
#                                                          if x[0] == x[0].lower()\
#                                                          else x)
#
#top_tracks_2022.drop(columns=['album'], inplace=True)
#top_tracks_2022.loc[7, 'track'] = 'Quevedo'




#top_tracks_2019 = pd.read_csv('Uncleaned data/Top tracks 2019.csv', encoding='utf-8-sig', index_col=0)
#top_tracks_2019.drop_duplicates(inplace=True)
#top_tracks_2019.reset_index(drop=True, inplace=True)
#top_tracks_2019.drop(columns = ['Beats.Per.Minute', 'Energy', 'Danceability', 'Loudness..dB..', 
#                                'Liveness', 'Valence.', 'Length.', 'Acousticness..', 'Speechiness.'],
#                                inplace=True)
#top_tracks_2019.dropna(inplace=True)
#
#top_tracks_2019.rename(columns={'Track.Name':'track', 'Artist.Name':'artists',
#                                'Genre':'genres', 'Popularity':'popularity'}, inplace=True)
#top_tracks_2019.to_csv('Cleaned data/top_tracks_2019_cleaned.csv', index=True)
#
#pd.set_option('display.max_colwidth', None)
#
#top_tracks_2019['track'] = top_tracks_2019['track'].str.split(' - ').str[0]
#top_tracks_2019['track'] = top_tracks_2019['track'].str.replace(r'\s+\([^()]*\)$', '', regex=True)
#top_tracks_2019['track'] = top_tracks_2019['track'].str.capitalize()
#top_tracks_2019['genres'] = top_tracks_2019['genres'].str.capitalize()
#
#top_tracks_2019.to_csv('Cleaned data/top_tracks_2019_cleaned.csv', index=True)


'''
top_tracks_2020 = pd.read_csv('Uncleaned data/Top tracks 2020.csv')
top_tracks_2021 = pd.read_csv('Uncleaned data/Top tracks 2021.csv')
top_tracks_2022 = pd.read_csv('Uncleaned data/Top tracks 2022.csv')
top_tracks_2023 = pd.read_csv('Uncleaned data/Top tracks 2023.csv', encoding='ISO-8859-1')
top_tracks_2024 = pd.read_csv('Uncleaned data/Top tracks 2024.csv', encoding='ISO-8859-1')

#Shortening the dataframes with many rows down to 100.
top_tracks_2020 = top_tracks_2020.head(100)
top_tracks_2021 = top_tracks_2021.head(100)
top_tracks_2023 = top_tracks_2023.head(100)
top_tracks_2024 = top_tracks_2024.head(100)

#Removing any duplicate rows.
top_tracks_2019.drop_duplicates(inplace=True)
top_tracks_2020.drop_duplicates(subset='Title', inplace=True)
#top_tracks_2021.drop_duplicates(subset='song_name', inplace=True)
#top_tracks_2022.drop_duplicates(inplace=True)
#top_tracks_2023.drop_duplicates(inplace=True)
top_tracks_2024.drop_duplicates(subset='Track', inplace=True)

#Removing columns
top_tracks_2019.drop(columns = ['Beats.Per.Minute', 'Energy', 'Danceability', 'Loudness..dB..', 
                                'Liveness', 'Valence.', 'Length.', 'Acousticness..', 'Speechiness.'],
                                inplace=True)

top_tracks_2020.drop(columns = 'Country', inplace=True) 

columns_2021 = ['spotify_id', 'song_name', 'artist_name', 'song_popularity', 
           'album_release_date', 'album_release_year', 'album_release_month']
top_tracks_2021 = top_tracks_2021[columns_2021] #Selecting which columns to keep.

columns_2022 = ['Spotify ID', 'Artist IDs', 'Track Name', 'Album Name', 'Artist Name(s)', 
                'Release Date', 'Duration (ms)', 'Popularity', 'Added By', 'Added At',
                'Genres']
top_tracks_2022 = top_tracks_2022[columns_2022]

columns_2023 = ['track_name', 'artist(s)_name', 'artist_count', 'released_year',
                'released_month', 'released_day', 'in_spotify_playlists', 'in_spotify_charts',
                'streams', 'in_apple_playlists', 'in_apple_charts']
top_tracks_2023 = top_tracks_2023[columns_2023]


columns_2024 = ['Track', 'Album Name', 'Artist', 'Release Date', 'All Time Rank', 'Track Score', 
                'Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 
                'Spotify Popularity', 'YouTube Views', 'YouTube Likes', 'Apple Music Playlist Count']
top_tracks_2024 = top_tracks_2024[columns_2024]

#Removing any rows with missing values
top_tracks_2019.dropna(inplace=True)
top_tracks_2020.dropna(inplace=True)
top_tracks_2021.dropna(inplace=True)
top_tracks_2022.dropna(inplace=True)
top_tracks_2023.dropna(inplace=True)
top_tracks_2024.dropna(inplace=True)

top_tracks_2019.rename(columns={'Track.Name':'track', 'Artist.Name':'artists',
                                'Genre':'genres', 'Popularity':'popularity'}, inplace=True)

top_tracks_2020.rename(columns={'Artist':'artists', 'Date':'date','Rank':'rank',
                                'Streams':'streams', 'Title':'title'}, inplace=True)

top_tracks_2021.rename(columns={'Unnamed: 0':'index', 'song_name': 'track','artist_name':'artists', 'song_popularity':'popularity'}, inplace=True)

top_tracks_2022.rename(columns={'Spotify ID':'spotify_id', 'Artist IDs': 'artist_id', 'Track Name':'track',
                                'Album Name':'album', 'Artist Name(s)':'artists', 'Release Date':'release_date',
                                'Duration (ms)':'duration (ms)', 'Popularity':'popularity',
                                'Added By':'added_by', 'Added At':'added_at', 'Genres':'genres'}, inplace=True)

top_tracks_2023.rename(columns={'track_name':'track', 'artist(s)_name':'artists'}, inplace=True)

top_tracks_2024.rename(columns={'Track':'track', 'Album Name':'album_name', 'Artist':'artists', 'Release Date':'release_date',
                                'All Time Rank':'all_time_rank', 'Track Score':'track_score', 'Spotify Streams':'spotify_streams',
                                'Spotify Playlist Count':'spotify_playlist_count', 'Spotify Playlist Reach':'spotify_playlist_reach',
                                'Spotify Popularity':'spotify_popularity', 'YouTube Views':'youtube_views', 'YouTube Likes': 'youtube_likes',
                                'Apple Music Playlist Count':'apple_music_playlist_count'}, inplace=True)

#top_tracks_2024.to_csv('Cleaned data/top_tracks_2024_cleaned.csv', index=True)

'''
#top_tracks_2019 = pd.read_csv('Cleaned data/top_tracks_2019_cleaned.csv', encoding='cp1252')
#pd.set_option('display.max_colwidth', None)
#
##top_tracks_2019.to_csv('Cleaned data/top_tracks_2019_cleaned.csv', index=True)
#print(top_tracks_2019)
#with open('Cleaned data/top_tracks_2019_cleaned.csv') as f:
#    print(f)