DIMENSIONS = [
    "Reasoning Transparency",
    "User Override Capability",
    "Skill Development",
    "No Decision Outsourcing",
    "Transparency at Use",
]

MIN_DIMENSION_SCORE = 1
MAX_DIMENSION_SCORE = 5


def get_maximum_total_score() -> int:
    """
    Return the maximum possible HJPI score
    based on the number of dimensions.
    """
    return len(DIMENSIONS) * MAX_DIMENSION_SCORE
