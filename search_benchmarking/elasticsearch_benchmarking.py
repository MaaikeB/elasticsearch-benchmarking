from utils.scoring import default_scoring_function


def perform_search(es_client, searches, index_name):
    # Loop over the Searches, run the search at ElasticSearch, compare the results with the expected results, and give a scoring
    for search in searches:
        # Get the search and expected results
        es_search = search['search']
        expected_results = search['expected_results']

        # Run the search at ElasticSearch
        es_results = es_client.search(
            index=index_name,
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
