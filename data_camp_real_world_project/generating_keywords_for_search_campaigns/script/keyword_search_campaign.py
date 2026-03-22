import pandas as pd

products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop']
keywords_list = []

for product in products: 
    for word in words:
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])

keywords_df = pd.DataFrame(keywords_list, columns=['Ad Group', 'Keyword'])
keywords_df['Campaign'] = 'SEM_Sofas'
keywords_df['Criterion Type'] = 'Exact'

keywords_df.to_csv('data/keywords.csv', index=False)