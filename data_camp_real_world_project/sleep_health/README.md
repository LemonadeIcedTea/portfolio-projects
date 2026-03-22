Sleep Health Data Analysis

In this project I'm tasked with identifying which occupation has the lowest sleep duration, which occupation has the lowest average sleep quality and whether the occupation with the lowest sleep duration is the same with the lowest sleep quality. Next I'm tasked with calculating the ratio of users diagnosed with insomnia for each BMI Category.

Output
- Occupation with the Lowest Sleep Duration
  Imported the sleep health dataset, grouped records by occupation and average sleep duration, then sorted the results to identify the occupation with the lowest sleep duration.

- Occupation with the Lowest Sleep Quality  
  Using a similar grouping approach, calculated average sleep quality by occupation and sorted the results. The occupation with the lowest sleep quality turned out to be the same as the one with the lowest sleep duration.

- BMI Category and Insomnia Rate
  Subset individuals by BMI category (normal, overweight, obese) and calculated insomnia rates by dividing the number of people with insomnia in each category by the total population of that category. Stored the ratios in a dictionary for comparison.

git clone https://github.com/LemonadeIcedTea/portfolio-projects.git
cd portfolio-projects/sleep_health

Instruction to Run the Code:
python script/sleep_health_data_analysis.py