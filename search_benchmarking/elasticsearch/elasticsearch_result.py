from search_benchmarking.result import Result



class ElasticSearchResult(Result):

    def __init__(self, fields, position):
        self.fields = fields
        self.position = position
