from search_benchmarking.query import Query

class ElasticSearchQuery(Query):

    def __init__(self, term, filters={}):
        self.term = term
        self.filters = filters

        # TODO: build the query

        # self.query = {
        #   "query": {"match_all": {}},
        #   "size": 10
        # }

        self.query = {
          "query": {"match": {"Posting Type": 'Internal'}},
          "size": 10
        }

        # 'Posting Type':'Internal'

        # self.query = {
        #   "query": {"match": {"Agency": term}},
        #   "size": 10
        # }