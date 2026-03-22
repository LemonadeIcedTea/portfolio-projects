Avocado Toast Supply Chain Analysis

In this project I'm tasked with finding out name of the countries that import avocadoes, olive oil and sourdough for creating Avocado Toast in the United Kingdom.

Output
- Top Avocado Origin in the United Kingdom
  Defined a function to read CSV files, retain only relevant columns, and create a categories_list column by splitting category tags. 
  
  The function drops rows with missing values, filters for relevant categories (loaded from a TXT file), and further narrows the dataset to entries located in the United Kingdom. 
  
  It then determines the most common origin country, cleans the country names by removing the en: prefix and replacing hyphens with spaces, prints the result, and returns top_origin_country.

- Top Olive Oil Origin in the United Kingdom
  Applied the same function to the olive oil dataset with its relevant categories to identify the leading origin country.

- Top Sourdough Origin in the United Kingdom
  Reused the function on the sourdough dataset and its categories to determine the most common origin country.

git clone https://github.com/LemonadeIcedTea/portfolio-projects.git
cd portfolio-projects/avocado_toast_supply_chain_analysis


Instruction to Run the Code:
python script/avocado_toast_supply_chain.py