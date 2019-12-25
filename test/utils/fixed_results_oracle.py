from search_benchmarking.elasticsearch.elasticsearch_query import ElasticSearchQuery
from search_benchmarking.elasticsearch.elasticsearch_result import ElasticSearchResult
from search_benchmarking.result import Result
from search_benchmarking.results_oracle import ResultsOracle




class FixedResultsOracle(ResultsOracle):

    def __init__(self, fixed_results: [Result]):
        self.fixed_results = fixed_results

    def search(self, query: ElasticSearchQuery) -> [ElasticSearchResult]:
        return self.fixed_results