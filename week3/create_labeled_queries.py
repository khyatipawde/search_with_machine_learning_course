import os
import argparse
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv
import re
from IPython.display import display

import nltk
stemmer = nltk.stem.PorterStemmer()

# Useful if you want to perform stemming.
import nltk
stemmer = nltk.stem.PorterStemmer()

categories_file_name = r'/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'

queries_file_name = r'/workspace/datasets/train.csv'
output_file_name = r'/workspace/datasets/labeled_query_data.txt'

parser = argparse.ArgumentParser(description='Process arguments.')
general = parser.add_argument_group("general")
general.add_argument("--min_queries", default=10000, help="The minimum number of queries per category label (default is 1)")
general.add_argument("--output", default=output_file_name, help="the file to output to")

args = parser.parse_args()
output_file_name = args.output

if args.min_queries:
    min_queries = int(args.min_queries)

# The root category, named Best Buy with id cat00000, doesn't have a parent.
root_category_id = 'cat00000'

tree = ET.parse(categories_file_name)
root = tree.getroot()

# Parse the category XML file to map each category id to its parent category id in a dataframe.
categories = []
parents = []
for child in root:
    id = child.find('id').text
    cat_path = child.find('path')
    cat_path_ids = [cat.find('id').text for cat in cat_path]
    leaf_id = cat_path_ids[-1]
    if leaf_id != root_category_id:
        categories.append(leaf_id)
        parents.append(cat_path_ids[-2])
parents_df = pd.DataFrame(list(zip(categories, parents)), columns =['category', 'parent'])

# Read the training data into pandas, only keeping queries with non-root categories in our category tree.
df = pd.read_csv(queries_file_name)[['category', 'query']]
df = df[df['category'].isin(categories)]

# IMPLEMENT ME: Convert queries to lowercase, and optionally implement other normalization, like stemming.
df['query'] = df['query'].str.lower()
# normalize? df['query'].apply(lambda x:(re.sub("[^A-Za-z0-9 ]","", x)))
df['tokens'] = df['query'].str.split()
df['stemmed_tokens'] = df['tokens'].apply(lambda x: [stemmer.stem(y) for y in x])
df['query'] = df['stemmed_tokens'].str.join(' ')
display(df)

# IMPLEMENT ME: Roll up categories to ancestors to satisfy the minimum number of queries per category.
parents_dict = parents_df.set_index("category")["parent"]
parents_dict[root_category_id] = root_category_id

def count_categories_below_threshold():
    return (df["category"].value_counts() < min_queries).sum()

categories_below_threshold = count_categories_below_threshold()
print('Init: Categories below threshold: ', categories_below_threshold)

while categories_below_threshold > 0:
    categories_below_threshold_df = df["category"].value_counts().where(lambda x: x < min_queries).dropna()
    df["category"] = df["category"].apply(lambda x: parents_dict[x] if x in categories_below_threshold_df else x)
    categories_below_threshold = count_categories_below_threshold()
    print('Checkpoint: Categories below threshold: ', categories_below_threshold)

# Print the distinct categories 
category_count = len(pd.unique(df['category']))
print('Distinct categories :', category_count)

# Create labels in fastText format.
df['label'] = '__label__' + df['category']

# Output labeled query data as a space-separated file, making sure that every category is in the taxonomy.
df = df[df['category'].isin(categories)]
df['output'] = df['label'] + ' ' + df['query']
df[['output']].to_csv(output_file_name, header=False, sep='|', escapechar='\\', quoting=csv.QUOTE_NONE, index=False)

## COMMANDS FOR 1(b) ##
# shuf /workspace/datasets/labeled_query_data.txt > /workspace/datasets/labeled_queries.txt
# head -50000 /workspace/datasets/labeled_queries.txt > /workspace/datasets/training_labeled_queries.txt
# tail -10000 /workspace/datasets/labeled_queries.txt > /workspace/datasets/test_labeled_queries.txt
# cd /workspace/datasets
# ~/fastText-0.9.2/fasttext supervised -input training_labeled_queries.txt -output labeled_queries_model -epoch 25
# ~/fastText-0.9.2/fasttext test labeled_queries_model.bin test_labeled_queries.txt

# head -100000 labeled_queries.txt > training_labeled_queries.txt
# ~/fastText-0.9.2/fasttext supervised -input training_labeled_queries.txt -output labeled_queries_model -epoch 25
# ~/fastText-0.9.2/fasttext test labeled_queries_model.bin test_labeled_queries.txt {1,2,3,5}
