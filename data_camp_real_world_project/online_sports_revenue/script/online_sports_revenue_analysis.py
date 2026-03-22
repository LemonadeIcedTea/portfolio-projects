import pandas as pd

brands = pd.read_csv('data/brands.csv')
finance = pd.read_csv('data/finance.csv')
info = pd.read_csv('data/info.csv')
reviews = pd.read_csv('data/reviews.csv')

sports_df = brands.merge(finance, on='product_id')
sports_df = sports_df.merge(info, on='product_id')
sports_df = sports_df.merge(reviews, on='product_id')
sports_df.dropna(inplace=True)
#sports_df.head()

labels = ['Budget', 'Average', 'Expensive', 'Elite']
sports_df['price_label'] = pd.qcut(sports_df['listing_price'], 4, labels=labels)
#sports_df.head()

adidas_vs_nike = sports_df.groupby(['brand', 'price_label'], as_index=False).agg(num_products=('price_label', 'count'), mean_revenue=('revenue', 'mean')).round(2)
print(adidas_vs_nike)

sports_df['description_length'] = sports_df['description'].str.len()
limits = [0, 100, 200, 300, 400, 500, 600, 700]
labels = ['100', '200', '300', '400', '500', '600', '700']
sports_df['description_length'] = pd.cut(sports_df['description_length'], bins=limits, labels=labels)

description_lengths = sports_df.groupby('description_length', as_index=False).agg(mean_rating=('rating', 'mean'), total_reviews=('reviews', 'sum')).round(2)
print(description_lengths)