import pandas as pd
import matplotlib.pyplot as plt

df_workout = pd.read_csv("data/workout.csv")

plt.figure(figsize=(12, 6))
plt.plot(df_workout["month"], df_workout["workout_worldwide"])
plt.xticks(rotation=90)
plt.show()

# Find the month where workout_worldwide peaked, take the year and convert it to a string type
year_str = str(pd.to_datetime(df_workout.loc[df_workout["workout_worldwide"].idxmax(), "month"]).year)
print(year_str, '\n')

df_keywords = pd.read_csv("data/three_keywords.csv")

plt.figure(figsize=(12, 6))
plt.plot(df_keywords["month"], df_keywords["home_workout_worldwide"], label="Home workout")
plt.plot(df_keywords["month"], df_keywords["gym_workout_worldwide"], label="Gym workout")
plt.plot(df_keywords["month"], df_keywords["home_gym_worldwide"], label="Home gym")
plt.xticks(rotation=90)
plt.legend()
plt.show()

# Hardcoded: represents a known historical context (COVID peak behavior), not derivable from data alone
peak_covid = "home workout"
# Drop 'month' so only keyword values are compared in the latest row
current = df_keywords.drop(columns="month").iloc[-1].idxmax()
print(peak_covid)
print(current, '\n')

df_workout_geo = pd.read_csv("data/workout_geo.csv", index_col = 0)
print(df_workout_geo.loc["United States"])
print(df_workout_geo.loc["Australia"])
print(df_workout_geo.loc["Japan"])

# Find which of United States, Australia, or Japan has the highest total interest across all workout types
top_country = df_workout_geo.loc[['United States', 'Australia', 'Japan']].sum(axis=1).idxmax()
print(top_country, '\n')

df_keywords_geo = pd.read_csv("data/three_keywords_geo.csv", index_col = 0)
print(df_keywords_geo.loc["Philippines", :])
print(df_keywords_geo.loc["Malaysia", :])

# Find whether Malaysia or Philippines has higher home workout interest
home_workout_geo = df_keywords_geo.loc[['Malaysia', 'Philippines'], 'home_workout_2018_2023'].idxmax()
print(home_workout_geo)