import elasticsearch

from search_benchmarking.elasticsearch.elasticsearch_query import ElasticSearchQuery
from search_benchmarking.results_oracle import ResultsOracle
from search_benchmarking.elasticsearch.elasticsearch_result import ElasticSearchResult



class ElasticSearchResultsOracle(ResultsOracle):

    def __init__(self, es_host, es_port, index, doc_type):
        self.es_client = elasticsearch.Elasticsearch([dict(host=es_host, port=es_port)], timeout=60)
        self.index = index
        self.doc_type = doc_type

    def search(self, query: ElasticSearchQuery) -> [ElasticSearchResult]:

        # Perform the ElasticSearch query
        es_results = self.es_client.search(
            index=self.index,
            doc_type=self.doc_type,
            body=query
        )

        # Return a list of ElasticSearchResult objects
        return [ElasticSearchResult(result['_source'], idx) for idx, result in enumerate(es_results['hits']['hits'])]
