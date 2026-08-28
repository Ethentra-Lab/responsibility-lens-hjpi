
from hjpi.methodology import DIMENSIONS

MIN_DIMENSION_SCORE = 1
MAX_DIMENSION_SCORE = 5


def get_maximum_total_score() -> int:
    """
    Return the maximum possible HJPI score
    based on the number of dimensions.
    """
    return len(DIMENSIONS) * MAX_DIMENSION_SCORE
