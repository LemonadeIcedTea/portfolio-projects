import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("data/netflix_data.csv")

filtered_df = netflix_df[(netflix_df['type'] == 'Movie') & (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]
filtered_df.head()

duration = filtered_df['duration'].value_counts().idxmax()
print(duration)

plt.figure(figsize=(12,6))
plt.hist(filtered_df['duration'], bins=20, color='skyblue')
plt.title('Distribution of Movie Durations (1990-1999)')
plt.xlabel('Duration in Minutes')
plt.ylabel('Number of Movies')
plt.grid(axis='y', alpha=0.75)
plt.show()

action_df = filtered_df[filtered_df['genre'] == 'Action']
short_movie_count = (action_df['duration'] < 90).sum()

print(short_movie_count)