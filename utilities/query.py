# A simple client for querying driven by user input on the command line.  Has hooks for the various
# weeks (e.g. query understanding).  See the main section at the bottom of the file
from opensearchpy import OpenSearch
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import argparse
import json
import os
from getpass import getpass
from urllib.parse import urljoin
import pandas as pd
import fasttext
import fileinput
import logging
import re


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(levelname)s:%(message)s')


model = fasttext.load_model('../datasets/labeled_queries_model.bin')

# expects clicks and impressions to be in the row
def create_prior_queries_from_group(
        click_group):  # total impressions isn't currently used, but it mayb worthwhile at some point
    click_prior_query = ""
    # Create a string that looks like:  "query": "1065813^100 OR 8371111^89", where the left side is the doc id and the right side is the weight.  In our case, the number of clicks a document received in the training set
    if click_group is not None:
        for item in click_group.itertuples():
            try:
                click_prior_query += "%s^%.3f  " % (item.doc_id, item.clicks / item.num_impressions)

            except KeyError as ke:
                pass  # nothing to do in this case, it just means we can't find priors for this doc
    return click_prior_query


# expects clicks from the raw click logs, so value_counts() are being passed in
def create_prior_queries(doc_ids, doc_id_weights,
                         query_times_seen):  # total impressions isn't currently used, but it mayb worthwhile at some point
    click_prior_query = ""
    # Create a string that looks like:  "query": "1065813^100 OR 8371111^89", where the left side is the doc id and the right side is the weight.  In our case, the number of clicks a document received in the training set
    click_prior_map = ""  # looks like: '1065813':100, '8371111':809
    if doc_ids is not None and doc_id_weights is not None:
        for idx, doc in enumerate(doc_ids):
            try:
                wgt = doc_id_weights[doc]  # This should be the number of clicks or whatever
                click_prior_query += "%s^%.3f  " % (doc, wgt / query_times_seen)
            except KeyError as ke:
                pass  # nothing to do in this case, it just means we can't find priors for this doc
    return click_prior_query


# Hardcoded query here.  Better to use search templates or other query config.
def create_query(user_query, click_prior_query, filters, sort="_score", sortDir="desc", size=10, source=None, name_param="name", categories=None, boost=False):
    #print("Pre-category filters are: ", filters)
    query_filters = filters
    category_boost = {}
    if categories:
        print("Selected Categories are: ", categories)
        if boost:
            category_boost = {
                "terms": 
                    {
                        "categoryPathIds": categories,
                        "boost": 10.0
                    }
            }
        else:
            category_filter = {
                "terms": {
                    "categoryPathIds": categories,
                }
            }
            if query_filters:
                query_filters.append(category_filter)
            else:
                query_filters = category_filter
    
    match_conditions = [  
                            {
                                "match": {
                                    name_param: {
                                        "query": user_query,
                                        "fuzziness": "1",
                                        "prefix_length": 2,
                                        # short words are often acronyms or usually not misspelled, so don't edit
                                        "boost": 0.01
                                    }
                                }
                            },
                            {
                                "match_phrase": {  # near exact phrase match
                                    "name.hyphens": {
                                        "query": user_query,
                                        "slop": 1,
                                        "boost": 50
                                    }
                                }
                            },
                            {
                                "multi_match": {
                                    "query": user_query,
                                    "type": "phrase",
                                    "slop": "6",
                                    "minimum_should_match": "2<75%",
                                    "fields": [f"{name_param}^10", "name.hyphens^10", "shortDescription^5",
                                               "longDescription^5", "department^0.5", "sku", "manufacturer", "features",
                                              ]
                                }
                            },
                            {
                                "terms": {
                                    # Lots of SKUs in the query logs, boost by it, split on whitespace so we get a list
                                    "sku": user_query.split(),
                                    "boost": 50.0
                                }
                            },
                            {  # lots of products have hyphens in them or other weird casing things like iPad
                                "match": {
                                    "name.hyphens": {
                                        "query": user_query,
                                        "operator": "OR",
                                        "minimum_should_match": "2<75%"
                                    }
                                }
                            }
    ]

    if boost:
        match_conditions.append(category_boost)

    query_obj = {
        'size': size,
        "sort": [
            { 
                sort : {
                    "order": sortDir
                }
            }
        ],
        "query": {
            "function_score": {
                "query": {
                    "bool": {
                        "must": [],
                        "should": match_conditions,
                        "minimum_should_match": 1,
                        "filter": query_filters  # filter by category
                    }
                },
                "boost_mode": "multiply",  # how _score and functions are combined
                "score_mode": "sum",  # how functions are combined
                "functions": [
                    {
                        "filter": {
                            "exists": {
                                "field": "salesRankShortTerm"
                            }
                        },
                        "gauss": {
                            "salesRankShortTerm": {
                                "origin": "1.0",
                                "scale": "100"
                            }
                        }
                    },
                    {
                        "filter": {
                            "exists": {
                                "field": "salesRankMediumTerm"
                            }
                        },
                        "gauss": {
                            "salesRankMediumTerm": {
                                "origin": "1.0",
                                "scale": "1000"
                            }
                        }
                    },
                    {
                        "filter": {
                            "exists": {
                                "field": "salesRankLongTerm"
                            }
                        },
                        "gauss": {
                            "salesRankLongTerm": {
                                "origin": "1.0",
                                "scale": "1000"
                            }
                        }
                    },
                    {
                        "script_score": {
                            "script": "0.0001"
                        }
                    }
                ]

            }
        }
    }
    if click_prior_query is not None and click_prior_query != "":
        query_obj["query"]["function_score"]["query"]["bool"]["should"].append({
            "query_string": {
                # This may feel like cheating, but it's really not, esp. in ecommerce where you have all this prior data,  You just can't let the test clicks leak in, which is why we split on date
                "query": click_prior_query,
                "fields": ["_id"]
            }
        })
    if user_query == "*" or user_query == "#":
        # replace the bool
        try:
            query_obj["query"] = {"match_all": {}}
        except:
            print("Couldn't replace query for *")
    if source is not None:  # otherwise use the default and retrieve all source
        query_obj["_source"] = source
    return query_obj

import nltk
stemmer = nltk.stem.PorterStemmer()

def normalize_query(query: str) -> str:
    words = query.split()
    stemmed_tokens = [stemmer.stem(x) for x in words]
    normalized_query = ' '.join(stemmed_tokens)
    return normalized_query

def search(client, user_query, index="bbuy_products", sort="_score", sortDir="desc", nameParam="name", catThreshold=0.0, boost=False, useMultipleProbabilities=True):
    #### W3: classify the query
    normalized_query = normalize_query(user_query)
    category_labels, probabilities = model.predict(normalized_query, k=5)
    print(f'Query: {normalized_query}')
    print(f'Labels: {category_labels}, Prob: {probabilities}')
    #### W3: create filters and boosts
    predicted_categories = []
    sum_of_probs = 0
    if (catThreshold):
        for i in range(len(probabilities)):
            category = category_labels[i][len("__label__"):]
            if useMultipleProbabilities:
                sum_of_probs += probabilities[i]
                predicted_categories.append(category)
                print(f'Category: {category}, Prob: {probabilities[i]}, Sum: {sum_of_probs}')
                
                if sum_of_probs > catThreshold:
                    break

            elif probabilities[i] > catThreshold:
                predicted_categories.append(category)
                print(f'Category: {category}, Prob: {probabilities[i]}')
        
    # Note: you may also want to modify the `create_query` method above
    query_obj = create_query(user_query, click_prior_query=None, filters=None, sort=sort, sortDir=sortDir, source=["name", "shortDescription","salesRankShortTerm","categoryPathIds","categoryPath"], name_param=nameParam, categories=predicted_categories, boost=boost)
    logging.info(query_obj)
    response = client.search(query_obj, index=index)
    if response and response['hits']['hits'] and len(response['hits']['hits']) > 0:
        hits = response['hits']['hits']
        # print(json.dumps(response, indent=2))
        for entry in response["hits"]["hits"]:
            print("Name: ", entry["_source"]["name"])
            #print("Short Desc: ", entry["_source"]["shortDescription"])
            #print("Sales Rank: ", entry["_source"]["salesRankShortTerm"])
            print("Categories: ", entry["_source"]["categoryPath"])
            print("Category IDs: ", entry["_source"]["categoryPathIds"])
            matching_categories = []
            for id in entry["_source"]["categoryPathIds"]:
                if id in predicted_categories:
                    matching_categories.append(id)
            print("Matching Category IDs: ", matching_categories)
            print("===================================================")


if __name__ == "__main__":
    host = 'localhost'
    port = 9200
    auth = ('admin', 'admin')  # For testing only. Don't store credentials in code.
    parser = argparse.ArgumentParser(description='Build LTR.')
    general = parser.add_argument_group("general")
    general.add_argument("-i", '--index', default="bbuy_products",
                         help='The name of the main index to search')
    general.add_argument("-s", '--host', default="localhost",
                         help='The OpenSearch host name')
    general.add_argument("-p", '--port', type=int, default=9200,
                         help='The OpenSearch port')
    general.add_argument('--user',
                         help='The OpenSearch admin.  If this is set, the program will prompt for password too. If not set, use default of admin/admin')
    general.add_argument("-y", '--synonyms', type=bool, default=False,
                         help='If set, uses name.synonyms instead of just name')
    general.add_argument("-t", '--prob_threshold', type=float, default=0.5,
                         help='Only use predicted categories with a higher threshold for filtering or boosting.')                     
    general.add_argument("-b", '--boost', type=bool, default=False,
                         help='If set, we boost using predicted categories for queries')

    args = parser.parse_args()

    if len(vars(args)) == 0:
        parser.print_usage()
        exit()

    host = args.host
    port = args.port
    if args.user:
        password = getpass()
        auth = (args.user, password)

    base_url = "https://{}:{}/".format(host, port)
    opensearch = OpenSearch(
        hosts=[{'host': host, 'port': port}],
        http_compress=True,  # enables gzip compression for request bodies
        http_auth=auth,
        # client_cert = client_cert_path,
        # client_key = client_key_path,
        use_ssl=True,
        verify_certs=False,  # set to true if you have certs
        ssl_assert_hostname=False,
        ssl_show_warn=False,

    )
    index_name = args.index
    query_prompt = "\nEnter your query (type 'Exit' to exit or hit ctrl-c):"
    print(query_prompt)
    for line in fileinput.input():
        query = line.rstrip()
        if query == "Exit":
            break
       
        name_param = "name.synonyms" if args.synonyms else "name"
        print(f"Name Param is {name_param}")

        prob_threshold = args.prob_threshold
        boost = args.boost

        search(client=opensearch, user_query=query, index=index_name, sort="_score", nameParam=name_param, catThreshold=prob_threshold, boost=boost)

        print(query_prompt)

    