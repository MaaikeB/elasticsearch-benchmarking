import argparse
import json
import os

import elasticsearch

from utils.scoring import default_scoring_function



DATAPACKAGE = 'data/datapackage.json'
ES_HOST = os.environ.get('ES_HOST', 'localhost')
ES_PORT = int(os.environ.get('ES_PORT', '9200'))
INDEX_NAME = 'jobs'

# Create the ElasticSearch client
es_client = elasticsearch.Elasticsearch([dict(host=ES_HOST, port=ES_PORT)], timeout=60)

# Add named command line arguments to the tool
parser = argparse.ArgumentParser()
parser.add_argument('--config_file_path', help='The path to the config file with the queries and expected results')
parser.add_argument('--index_name', help='The ElasticSearch index to query')



if __name__ == "__main__":

    # Parse the command line arguments
    args = parser.parse_args()
    config_file_path = args.config_file_path
    index_name = args.index_name

    # Read the config file
    with open(config_file_path) as config_file:
        config = json.load(config_file)

    # Loop over the Searches, run the search at ElasticSearch, compare the results with the expected results, and give a scoring
    for search in config['searches']:
        # Get the search and expected results
        es_search = search['search']
        expected_results = search['expected_results']

        # Run the search at ElasticSearch
        es_results = es_client.search(
                        index=INDEX_NAME,
                        doc_type='jobs',
                        body=es_search
        )

    # Get the positions of the expected results in the actual results (it at all)
    expected_results_positions = [None for i in expected_results]
    # Loop over the actual results
    for results_idx, result in enumerate(es_results['hits']['hits']):
        # Run over the expected results
        for expected_results_idx, expected_result in enumerate(expected_results):
            # If the actual result is in the list of expected results, save it's position, at its index
            if result['_id'] == expected_result:
                expected_results_positions[expected_results_idx] = results_idx

    # Pass the positions of the expected results to the scoring function
    scoring = default_scoring_function(expected_results_positions, len(es_results))

    print(scoring)
