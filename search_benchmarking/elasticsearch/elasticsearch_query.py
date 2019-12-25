from search_benchmarking.query import Query

class ElasticSearchQuery(Query):

    def __init__(self, term, filters={}):
        self.term = term
        self.filters = filters
        self.query = term

    # TODO: build the query class, so you can create something like the below
    # search = {
    #     "bool": {
    #         "must": {"match": {"title": "how to make millions"}},
    #         "must_not": {"match": {"tag": "spam"}},
    #         "should": [
    #             {"match": {"tag": "starred"}}
    #         ],
    #         "filter": {
    #             "bool": {
    #                 "must": [
    #                     {"range": {"date": {"gte": "2014-01-01"}}},
    #                     {"range": {"price": {"lte": 29.99}}}
    #                 ],
    #                 "must_not": [
    #                     {"term": {"category": "ebooks"}}
    #                 ]
    #             }
    #         }
    #     }
    # }

