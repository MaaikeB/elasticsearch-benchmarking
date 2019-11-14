
def default_scoring_function(expected_results_positions, results_amount):
    """
    Calculates a scoring of ElasticSearch results, based on the positions of the expected results, and the total amount
    of results

    For example
    - The expected results are [1,2] and the actual results are [0,1,2,3,4], the expected results are on
    position 2 and 3 and the scoring will be 0.8
    - The expected results are [1,2] and the actual results are [0,1,2,3,4,5,6,7,8,9], the expected results are on
    position 2 and 3 and the scoring will be 0.9(since there are a total of 10 results)


    :param (list) expected_results_positions: A list of the positions of the expected results
    :return (int): The scoring, which can range from 0-1
    """

    # Get the 'distances' of the actual results compared to the expected results.
    # For example, if the expected results are [1,2] and the actual results are [0,1,2] the average distance is 1,
    # because the expected results do not come on the 1th and 2nd results but on the 2nd and the 3rd
    index = 0
    distances = []
    for expected_results_position in expected_results_positions:
        distances.append(expected_results_position - index)
        index += 1

    average_distance = sum(distances)/len(distances)

    factor = results_amount/1
    score = 1-(average_distance/factor)

    return score