import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 12

label_customization = dict({'fontsize': 14, 'weight':'bold'})

most_popular_2022 = pd.read_csv('Cleaned data/top_tracks_2022_cleaned.csv')

most_popular_2022.sort_values('popularity', ascending=True, inplace=True)
popular_10_2022 = most_popular_2022[['track', 'popularity']].tail(10)

fig, ax = plt.subplots()

ax.barh(popular_10_2022['track'], popular_10_2022['popularity'], color='#CAF4F4', 
        edgecolor='black')
ax.set_title('Most Popular Tracks of 2022', fontsize=18, weight='bold', pad=20)

ax.set_xlabel('Popularity Scale [0 – 100]', **label_customization)
ax.set_ylabel('Name of Tracks', **label_customization)
ax.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_xlim((0.0, 100.0))

plt.locator_params(axis='x', nbins=10)
plt.grid()
plt.savefig('Visualizations/Most Popular Songs 2022.jpg', bbox_inches='tight', dpi=300)
plt.show()