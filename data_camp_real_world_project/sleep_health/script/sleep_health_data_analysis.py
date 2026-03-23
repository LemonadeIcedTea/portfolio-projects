import pandas as pd

sleep = pd.read_csv('data/sleep_health_data.csv')

sleep_duration = sleep.groupby('Occupation')['Sleep Duration'].mean()
lowest_sleep_occ = sleep_duration.sort_values().index[0]

print(lowest_sleep_occ)

sleep_quality = sleep.groupby('Occupation')['Quality of Sleep'].mean()
lowest_sleep_quality_occ = sleep_quality.sort_values().index[0]
print(lowest_sleep_quality_occ)

same_occ = lowest_sleep_occ == lowest_sleep_quality_occ

normal = sleep[(sleep['BMI Category'] == 'Normal') & (sleep['Sleep Disorder'] == 'Insomnia')]
total_normal = len(sleep[sleep['BMI Category'] == 'Normal'])
normal_insomnia_ratio = round(len(normal) / total_normal, 2)

overweight = sleep[(sleep['BMI Category'] == 'Overweight') & (sleep['Sleep Disorder'] == 'Insomnia')]
total_overweight = len(sleep[sleep['BMI Category'] == 'Overweight'])
overweight_insomnia_ratio = round(len(overweight) / total_overweight, 2)

obese = sleep[(sleep['BMI Category'] == 'Obese') & (sleep['Sleep Disorder'] == 'Insomnia')]
total_obese = len(sleep[sleep['BMI Category'] == 'Obese'])
obese_insomnia_ratio = round(len(obese) / total_obese, 2)

bmi_insomnia_ratios = {
    'Normal': normal_insomnia_ratio,
    'Overweight': overweight_insomnia_ratio,
    'Obese': obese_insomnia_ratio
}
print(bmi_insomnia_ratios)