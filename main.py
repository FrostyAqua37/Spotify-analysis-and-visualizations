import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

top_tracks_2024 = pd.read_csv('Cleaned data/top_tracks_2024_cleaned.csv')
top_10_tracks_2024 = top_tracks_2024[['artists', 'track', 'spotify_streams']].head(10)
top_10_tracks_2024.sort_values('spotify_streams', ascending=True, inplace=True)

label_customization = dict({'family':'Times New Roman', 'fontsize':18})

plt.barh(top_10_tracks_2024['track'], top_10_tracks_2024['spotify_streams'], color='#1ED760',
         edgecolor='black')
plt.title('Top 10 songs of 2024', family='Times New Roman', fontsize=20)
plt.xlabel('Number of Listeners', **label_customization)
plt.ylabel('Name of songs', **label_customization)
plt.ticklabel_format(style='plain', useOffset=False, axis='x')
plt.grid()


plt.show()