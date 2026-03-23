import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crimes = pd.read_csv("data/crimes.csv")
crimes.head()
# TIME OCC is stored as an integer in HHMM format (e.g., 730 = 7:30).
# Zero-pad to 4 digits, then take the first 2 digits as the hour (07 = 7 AM).
crimes["hour"] = crimes["TIME OCC"].astype(str).str.zfill(4).str[:2].astype(int)

peak_crime_hour = crimes["hour"].value_counts().idxmax()
print(peak_crime_hour)

hour_counts = crimes["hour"].value_counts().sort_index()

plt.figure(figsize=(12,6))
sns.barplot(x=hour_counts.index, y=hour_counts.values, color="skyblue")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Crimes")
plt.title("Number of Crimes by Hour of Day")
plt.xticks(range(0, 24))
plt.show()

night_crime = crimes[(crimes["TIME OCC"] >= 2200) | (crimes["TIME OCC"] <= 359)]
night_crime.head()

peak_night_crime_location = night_crime["AREA NAME"].value_counts().idxmax()
print(peak_night_crime_location)

night_crime_area_counts = night_crime["AREA NAME"].value_counts().sort_values(ascending=False)

plt.figure(figsize=(14,6))
sns.barplot(x=night_crime_area_counts.index, y=night_crime_area_counts.values, color="salmon")
plt.xlabel("Area Name")
plt.ylabel("Number of Night Crimes")
plt.title("Number of Night Crimes by Area")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

crimes["Vict Age"] = pd.to_numeric(crimes["Vict Age"], errors="coerce")

age_bins = [0, 17, 25, 34, 44, 54, 64, 150]
age_group_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

# Create a new column for victim age groups
crimes["Vict Age Group"] = pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_group_labels, right=True, include_lowest=True)

# Count the number of crimes in each age group
victim_ages = crimes["Vict Age Group"].value_counts().sort_index()
print(victim_ages)

plt.figure(figsize=(8,5))
sns.barplot(x=victim_ages.index, y=victim_ages.values)
plt.xlabel("Victim Age Group")
plt.ylabel("Number of Victims per Age Group")
plt.title("Distribution of Crimes committed against Victim's Age Group")
plt.show()