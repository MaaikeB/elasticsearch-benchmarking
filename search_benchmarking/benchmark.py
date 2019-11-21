from search_benchmarking.results_oracle import ResultsOracle
from search_benchmarking.query import Query
from search_benchmarking.scoring.scoring import Scoring



class Benchmark(object):

    def __init__(self, results_oracle: ResultsOracle, scorer: Scoring):
        self.results_oracle = results_oracle
        self.scorer = scorer

    def execute(self, searches: (Query, '')) -> int:

        # Perform the searches and save the results
        scores = []
        for query, expected_results in searches:
            results = self.results_oracle.search(query.query)

            # Get the scoring
            score = self.scorer.calculate_score(results, expected_results)
            scores.append(score)

        return sum(scores)/len(scores)
