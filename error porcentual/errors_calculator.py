
def percent_error(given_value, expected_value) -> float:

    result = (abs(given_value - expected_value)/expected_value)*100

    return result


def approximate_error(current_expected_value, prev_expected_value) -> float:
    result = (abs((current_expected_value - prev_expected_value)) /
              current_expected_value)*100
    return result


