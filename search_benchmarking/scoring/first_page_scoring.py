from search_benchmarking.scoring.scoring import Scoring



class FirstPageScorer(Scoring):

    def __init__(self, page_size, factor):
        self.page_size = page_size
        self.factor = factor

    def calculate_score(self, results, expected_results_function):
        score = 0
        for result in results:
            if expected_results_function(result.fields):
                score += 1

        return score/len(results)
