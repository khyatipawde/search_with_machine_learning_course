import pandas as pd

labeled_data_filename = '/workspace/datasets/fasttext/labeled_products.txt'
pruned_data_filename  = '/workspace/datasets/fasttext/pruned_labeled_products.txt'

threshold = 500

# read the whole row, and split later
df = pd.read_csv(labeled_data_filename, sep='\t', header=None, names=["row"])

df['label'] = df['row'].apply(lambda x: x.split(' ')[0])
df['title'] = df['row'].apply(lambda x: ' '.join(x.split(' ')[1:]))
df.drop(columns=['row'], inplace=True)

df_label_count = df.groupby('label').agg({'title': 'count'}).reset_index()
df_label_count.rename(columns={'title': 'title_count'}, inplace=True)
df = pd.merge(df, df_label_count, on='label')
df = df[df.title_count >= threshold]
df = df[['label', 'title']]
print(df.head())

df.to_csv(pruned_data_filename, header=False, index=False, sep=' ')