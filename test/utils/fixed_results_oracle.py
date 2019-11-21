from search_benchmarking.elasticsearch.elasticsearch_query import ElasticSearchQuery
from search_benchmarking.results_oracle import BaseResultOracle



class FixedResultsOracle(BaseResultOracle):

    def query(self, query: ElasticSearchQuery):
        # returns ElasticSearchResult[]
        pass