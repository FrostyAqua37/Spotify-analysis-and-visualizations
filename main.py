import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 12

label_customization = dict({'fontsize': 14, 'weight':'bold'})


top_tracks_2024 = pd.read_csv('Cleaned data/top_tracks_2024_cleaned.csv')
top_tracks_2024.sort_values('spotify_streams', ascending=True, inplace=True)
top_10_tracks_2024 = top_tracks_2024[['artists', 'track', 'spotify_streams']].tail(10)

fig, ax = plt.subplots()

ax.barh(top_10_tracks_2024['track'], top_10_tracks_2024['spotify_streams'], color='#4B0082',
         edgecolor='black')

#Text for title, X and Y Axis.
ax.set_title('Most Streamed Songs of 2024', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Number of streams (in billions)', **label_customization)
ax.set_ylabel('Top Tracks', **label_customization)

ax.set_xticklabels(['0', '0,5', '1', '1,5', '2', '2,5', '3', '3,5', '4'])

#Removes the outer lines except the bottom one
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#Space between axis text and chart.
plt.tick_params(axis='both', pad=10)
ax.grid()

plt.savefig('Visualizations/Most Streamed Songs 2024.jpg', bbox_inches='tight', dpi=300)

plt.show()

'''

top_tracks_2023 = pd.read_csv('Cleaned data/top_tracks_2023_cleaned.csv')
top_tracks_2023.sort_values('streams', ascending=True, inplace=True)
top_10_tracks_2023 = top_tracks_2023[['track', 'streams']].tail(10)

fig, ax = plt.subplots()
ax.barh(top_10_tracks_2023['track'], top_10_tracks_2023['streams'], color='#ff8c69', edgecolor='black')

plt.title('Most Streamed Songs of 2023', fontsize=18, weight='bold', pad=20)
plt.xlabel('Number of streams (in billions)', **label_customization, labelpad=15)
plt.ylabel('Top Tracks', **label_customization, labelpad=-10)
plt.grid()

ax.set_xticklabels(['0', '0,5', '1', '1,5', '2', '2,5', '3', '3,5'])
#Removes the outer lines except the bottom one
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#Space between axis text and chart.
plt.tick_params(axis='both', pad=10)

plt.autoscale(enable=True, axis='y', tight=True)
plt.savefig('Visualizations/Most Streamed Songs 2023.jpg', bbox_inches='tight', dpi=300)
plt.show()
'''