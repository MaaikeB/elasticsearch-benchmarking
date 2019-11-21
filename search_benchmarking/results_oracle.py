from search_benchmarking.query import Query
from search_benchmarking.result import Result


class ResultsOracle(object):

    def search(self, query: Query) -> [Result]:
        raise NotImplementedError()
