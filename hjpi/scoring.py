from collections.abc import Mapping, Sequence


MIN_DIMENSION_SCORE = 1
MAX_DIMENSION_SCORE = 5


def calculate_score(scores: Sequence[int]) -> tuple[int, float]:
    """
    Calculate the total HJPI score and percentage.

    Each dimension must be scored from 1 to 5.
    """

    if not scores:
        raise ValueError("At least one dimension score is required.")

    for score in scores:
        if not isinstance(score, int) or isinstance(score, bool):
            raise ValueError("Each dimension score must be an integer.")

        if score < MIN_DIMENSION_SCORE or score > MAX_DIMENSION_SCORE:
            raise ValueError(
                f"Each dimension score must be between "
                f"{MIN_DIMENSION_SCORE} and {MAX_DIMENSION_SCORE}."
            )

    total = sum(scores)
    maximum_possible = len(scores) * MAX_DIMENSION_SCORE
    percentage = (total / maximum_possible) * 100

    return total, percentage


def get_verdict(
    percentage: float,
    thresholds: Mapping[str, float],
    verdict_labels: Mapping[str, str],
) -> tuple[str, str]:
    """
    Determine the HJPI screening verdict for a percentage score.
    """

    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100.")

    if percentage >= thresholds["pass"]:
        return verdict_labels["PASS"], "PASS"

    if percentage >= thresholds["conditional"]:
        return verdict_labels["CONDITIONAL"], "CONDITIONAL"

    if percentage >= thresholds["redesign"]:
        return verdict_labels["REDESIGN"], "REDESIGN"

    return verdict_labels["FAIL"], "FAIL"