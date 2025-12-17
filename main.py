import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 12

top_tracks_2024 = pd.read_csv('Cleaned data/top_tracks_2024_cleaned.csv')
top_10_tracks_2024 = top_tracks_2024[['artists', 'track', 'spotify_streams']].head(10)
top_10_tracks_2024.sort_values('spotify_streams', ascending=True, inplace=True)

label_customization = dict({'fontsize': 14, 'weight':'bold',
                            'labelpad': 15})

fig, ax = plt.subplots(figsize=(8, 6))

ax.barh(top_10_tracks_2024['track'], top_10_tracks_2024['spotify_streams'], color='#4B0082',
         edgecolor='black')

#Text for title, X and Y Axis.
ax.set_title('Top 10 songs of 2024', fontsize=24, weight='bold', pad=20)
ax.set_xlabel('Number of listeners (in billions)', **label_customization)
ax.set_ylabel('Name of Songs', **label_customization)

ax.set_xticklabels(['0', '0,5', '1', '1,5', '2', '2,5', '3', '3,5', '4'])

#Removes the outer lines except the bottom one
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#Space between axis text and chart.
plt.tick_params(axis='both', pad=10)
ax.grid()

plt.savefig('Top 10 Tracks of 2024.jpg', bbox_inches='tight', dpi=300)
plt.show()