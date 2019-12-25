from search_benchmarking.result import Result



class Scoring(object):

    def calculate_score(self, results: [Result], expected_results: [Result]):
        raise NotImplementedError()
