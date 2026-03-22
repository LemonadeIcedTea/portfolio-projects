import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


shopping_data = pd.read_csv("data/online_shopping_session_data.csv")
shopping_data.head()

shopping_Nov_Dec = shopping_data[(shopping_data['Month'] == 'Nov') | (shopping_data['Month'] == 'Dec')]
shopping_Nov_Dec.head()

session_count = shopping_Nov_Dec.groupby('CustomerType')['Purchase'].value_counts()
print(session_count)

total_new_customer = np.sum(session_count['New_Customer'])
total_returning_customer = np.sum(session_count['Returning_Customer'])

new_customer_purchase = session_count['New_Customer', 1]
returning_customer_purchase = session_count['Returning_Customer', 1]

new_purchase_rate = new_customer_purchase / total_new_customer
returning_purchase_rate = returning_customer_purchase / total_returning_customer

purchase_rates = {'Returning_Customer': returning_purchase_rate, 'New_Customer': new_purchase_rate}
print(purchase_rates)

list_of_corr = shopping_Nov_Dec[['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration']].corr()
print(list_of_corr)

top_correlation = {'pair': ('Administrative_Duration', 'ProductRelated_Duration'), 'correlation': 0.389855}

increased_returning_purchase_rate = returning_purchase_rate * 1.15

sales_less_than_100 = stats.binom.cdf(k=100, n=500, p=increased_returning_purchase_rate)
print('Probabilty of sales less than 100:', sales_less_than_100)
prob_at_least_100_sales = 1 - sales_less_than_100
print('Probabilty of at least 100 sales:', prob_at_least_100_sales)

num_trials = 500
k_values = np.arange(500) + 1
p_binom_values = [stats.binom.pmf(k, num_trials, increased_returning_purchase_rate) for k in k_values]

plt.bar(k_values, p_binom_values)
plt.vlines(100, 0, 0.08, color='red', linestyle='dashed', label='sales=100')
plt.xlabel('number of sales')
plt.ylabel('probability')
plt.legend()
plt.show()