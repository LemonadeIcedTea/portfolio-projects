import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("data/netflix_data.csv")

filtered_df = netflix_df[(netflix_df['type'] == 'Movie') & (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]
filtered_df.head()

#duration = filtered_df['duration'].value_counts().idmax()
#print(duration)

plt.figure(figsize=(12,6))
plt.hist(filtered_df['duration'], bins=20, color='skyblue')
plt.title('Distribution of Movie Durations (1990-1999)')
plt.xlabel('Duration in Minutes')
plt.ylabel('Number of Movies')
plt.grid(axis='y', alpha=0.75)
plt.show()

duration = 100
print(duration)

action_df = filtered_df[filtered_df['genre'] == 'Action']
short_movie_count = 0

for label, row in action_df.iterrows():
    if row['duration'] < 90:
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count

print(short_movie_count)