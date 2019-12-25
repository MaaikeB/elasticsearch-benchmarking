import os

from search_benchmarking.benchmark import Benchmark
from search_benchmarking.elasticsearch.elasticsearch_results_oracle import ElasticSearchResultsOracle
from search_benchmarking.elasticsearch.elasticsearch_query import ElasticSearchQuery
from search_benchmarking.scoring.first_page_scoring import FirstPageScorer



ES_HOST = os.environ.get('ES_HOST', 'localhost')
ES_PORT = int(os.environ.get('ES_PORT', '9200'))


benchmark = Benchmark(
    results_oracle=ElasticSearchResultsOracle(ES_HOST, ES_PORT, index='jobs', doc_type='jobs'),
    scorer=FirstPageScorer(page_size=10, factor=0.87),
)

def expected_results(r):
    return r['Posting Type'] == 'Internal'

searches = [
    (ElasticSearchQuery({
          "query": {"match": {"Posting Type": 'Internal'}},
          "size": 10
        }), lambda r: r['Posting Type'] == 'Internal'),
]

score = benchmark.execute(searches)
print('score', score)
