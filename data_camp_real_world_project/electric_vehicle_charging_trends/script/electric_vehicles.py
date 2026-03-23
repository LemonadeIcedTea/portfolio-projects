import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

private_df = pd.read_csv('data/private_ev_charging.csv')
public_df = pd.read_csv('data/public_ev_charging.csv')
sales_df = pd.read_csv('data/ev_sales.csv')

total_sales = sales_df.groupby('year')['sales'].sum()
print(total_sales)
ev_sales_2018 = 361315.0
print(ev_sales_2018, '\n')

electric_charging = private_df.merge(public_df, on='year', how='inner')

electric_charging = electric_charging.merge(total_sales, on='year', how='left')
electric_charging = electric_charging.dropna(subset='sales')

fig, ax = plt.subplots()

sns.lineplot(data=electric_charging, x='year', y='private_ports', label='Private Ports')
sns.lineplot(data=electric_charging, x='year', y='public_ports', label='Public Ports')
sns.lineplot(data=electric_charging, x='year', y='sales', label='Total Sales')

ax.set_title('EV Ports and Sales Over Time')
ax.set(xlabel='Year', ylabel='Count')
ax.legend(loc='upper left')

plt.show()
trend = 'same'
print(trend)