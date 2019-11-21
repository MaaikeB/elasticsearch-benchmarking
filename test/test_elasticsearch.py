import os

import elasticsearch

from search_benchmarking.benchmark import Benchmark
from test.utils.fixed_results_oracle import FixedResultsOracle



ES_HOST = os.environ.get('ES_HOST', 'localhost')
ES_PORT = int(os.environ.get('ES_PORT', '9200'))

# Create the ElasticSearch client
es_client = elasticsearch.Elasticsearch([dict(host=ES_HOST, port=ES_PORT)], timeout=60)


def test_elasticsearch():
    test_benchmark = Benchmark(
        oracle=FixedResultsOracle(test_results),
        scorer=ConstScorer(5),
    )