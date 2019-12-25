import os
import unittest

from search_benchmarking.elasticsearch.elasticsearch_query import ElasticSearchQuery
from search_benchmarking.elasticsearch.elasticsearch_result import ElasticSearchResult
from search_benchmarking.elasticsearch.elasticsearch_results_oracle import ElasticSearchResultsOracle
from search_benchmarking.benchmark import Benchmark
from search_benchmarking.scoring.first_page_scoring import FirstPageScorer
from test.utils.fixed_results_oracle import FixedResultsOracle



ES_HOST = os.environ.get('ES_HOST', 'localhost')
ES_PORT = int(os.environ.get('ES_PORT', '9200'))




class TestElasticsearch(unittest.TestCase):

    def test_elasticsearch_example(self):
        """
        Example test ElasticSearch, searching for a term in a specific field
        """

        benchmark = Benchmark(
            results_oracle=ElasticSearchResultsOracle(ES_HOST, ES_PORT, index='jobs', doc_type='jobs'),
            scorer=FirstPageScorer(page_size=10, factor=0.87),
        )

        searches = [
            (ElasticSearchQuery({
                "query": {"match": {"Posting Type": 'Internal'}},
                "size": 10
            }), lambda r: r['Posting Type'] == 'Internal'),
        ]

        score = benchmark.execute(searches)
        self.assertEqual(score, 1)

    """
    Possible tests
    - searching for a term in all fields, for example the term 'Engineering' in all fields
    - searching for a phrase, for example 'Director, Infrastructure Build Coordinator'
    - performing a search where the result should not include a certain term, for example 'Posting Type' = 'Internal'
    """


class TestCode(unittest.TestCase):

    def test_fixed_results_example(self):
        """
        Example of a test with fixed results (doesn't use a search engine), in order to test the own code
        """

        test_results = [
            ElasticSearchResult({'Job type': 'Art'}, 0),
            ElasticSearchResult({'Job type': 'Art'}, 1),
            ElasticSearchResult({'Job type': 'Art'}, 2)
        ]

        test_benchmark = Benchmark(
            results_oracle=FixedResultsOracle(test_results),
            scorer=FirstPageScorer(10, 1),
        )

        searches = [
            (ElasticSearchQuery({
                "query": {"match": {"Job type": 'Art'}},
                "size": 10
            }), lambda r: r['Job type'] == 'Art'),
        ]

        score = test_benchmark.execute(searches)
        self.assertEqual(score, 1)



if __name__ == '__main__':
    unittest.main()