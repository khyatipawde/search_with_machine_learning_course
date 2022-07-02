import os
import random
import argparse
import fasttext
import csv
from pathlib import Path

directory = r'/workspace/datasets/fasttext'
SIMILARITY_THRESHOLD = 0.75

parser = argparse.ArgumentParser(description='Process some integers.')
general = parser.add_argument_group("general")
general.add_argument("--model_file", default=f"normalized_title_model.bin",  help="requires word representation model file")
general.add_argument("--top_words_file",  default=f"top_words.txt", help="text file containing the list of top words to find synonyms for")
general.add_argument("--output_file",  default=f"synonyms.csv", help="csv file to output the synonym mapping to")

args = parser.parse_args()

model_filepath = f"{directory}/{args.model_file}" 
model = fasttext.load_model(model_filepath)
print("Using model %s" % model_filepath)

top_words_filepath = f"{directory}/{args.top_words_file}"
print("Reading entries from %s" % top_words_filepath)

output_filepath    = f"{directory}/{args.output_file}"
print("Writing results to %s" % output_filepath)

with open(top_words_filepath, 'r') as top_words:
    with open(output_filepath, 'w') as output:
        writer = csv.writer(output)
        for word in top_words:
            data = [ word.strip() ]
            synonyms = model.get_nearest_neighbors(word)
            for (similarity_score, synonym) in synonyms:
                if similarity_score > SIMILARITY_THRESHOLD:
                    data.append(synonym)
            
            #print("Row is : ", data, end = '')
            writer.writerow(data)

