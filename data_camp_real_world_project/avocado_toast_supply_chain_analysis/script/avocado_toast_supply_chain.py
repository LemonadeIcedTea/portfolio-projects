import pandas as pd
from pathlib import Path

def read_and_filter_data(filename, relevant_categories): 
    df = pd.read_csv(Path('data') / filename, sep='\t', encoding='utf-8', low_memory=False)

    subset_columns = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins', 'origins_tags']
    df = df[subset_columns]

    df['categories_list'] = df['categories_tags'].str.split(',')

    df = df.dropna(subset = 'categories_list')

    df = df[df['categories_list'].apply(lambda x: any([i for i in x if i in relevant_categories]))]

    df_uk = df[df['countries'] == 'United Kingdom']

    top_origin = df_uk['origins_tags'].value_counts().index[0]
    top_origin_country = top_origin.lstrip("en:").replace('-', ' ')

    print(f'**{filename[:-4]} origins** \n', top_origin, '\n')
    print("Top origin country: ", top_origin_country, '\n')

    return top_origin_country 

with open("data/relevant_avocado_categories.txt", "r", encoding="utf-8") as file:
    relevant_avocado_categories = file.read().splitlines()

top_avocado_origin = read_and_filter_data('avocado.csv', relevant_avocado_categories)

with open("data/relevant_olive_oil_categories.txt", "r", encoding='utf-8') as file:
    relevant_olive_oil_categories = file.read().splitlines()

top_olive_oil_origin = read_and_filter_data('olive_oil.csv', relevant_olive_oil_categories)

with open("data/relevant_sourdough_categories.txt", "r", encoding='utf-8') as file: 
    relevant_sourdough_categories = file.read().splitlines()

top_sourdough_origin = read_and_filter_data('sourdough.csv', relevant_sourdough_categories)
