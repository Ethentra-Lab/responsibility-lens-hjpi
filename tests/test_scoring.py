import pytest

from hjpi.scoring import calculate_score, get_verdict

from hjpi.config import MAX_DIMENSION_SCORE
from hjpi.methodology import DIMENSIONS


def test_calculate_score_maximum():
    scores = [MAX_DIMENSION_SCORE] * len(DIMENSIONS)

    total, percentage = calculate_score(scores)

    assert total == len(DIMENSIONS) * MAX_DIMENSION_SCORE
    assert percentage == 100

def test_calculate_score_with_mixed_scores():
    scores = [5, 4, 3, 2, 1]

    total, percentage = calculate_score(scores)

    assert total == 15
    assert percentage == 60.0


def test_calculate_score_rejects_score_above_five():
    scores = [5, 5, 6, 4, 3]

    with pytest.raises(ValueError):
        calculate_score(scores)


def test_calculate_score_rejects_score_below_one():
    scores = [5, 4, 0, 3, 2]

    with pytest.raises(ValueError):
        calculate_score(scores)


def test_get_verdict_returns_pass():
    thresholds = {
        "pass": 80,
        "conditional": 60,
        "redesign": 40,
    }

    verdict_labels = {
        "PASS": "Pass",
        "CONDITIONAL": "Conditional",
        "REDESIGN": "Redesign",
        "FAIL": "Fail",
    }

    verdict, level = get_verdict(
        85,
        thresholds,
        verdict_labels,
    )

    assert verdict == "Pass"
    assert level == "PASS"


def test_get_verdict_returns_fail():
    thresholds = {
        "pass": 80,
        "conditional": 60,
        "redesign": 40,
    }

    verdict_labels = {
        "PASS": "Pass",
        "CONDITIONAL": "Conditional",
        "REDESIGN": "Redesign",
        "FAIL": "Fail",
    }

    verdict, level = get_verdict(
        30,
        thresholds,
        verdict_labels,
    )

    assert verdict == "Fail"
    assert level == "FAIL"