from hjpi.config import (
    MAX_DIMENSION_SCORE,
    get_maximum_total_score,
)
from hjpi.methodology import (
    DIMENSIONS,
    HJPI_DIMENSIONS,
)


def test_hjpi_has_six_dimensions():
    assert len(HJPI_DIMENSIONS) == 6


def test_dimension_names_match_methodology():
    expected_names = [
        dimension["name"]
        for dimension in HJPI_DIMENSIONS
    ]

    assert DIMENSIONS == expected_names


def test_all_dimensions_have_required_fields():
    required_fields = {
        "id",
        "icon",
        "name",
        "description",
        "screening_question",
        "indicators",
        "evidence_examples",
    }

    for dimension in HJPI_DIMENSIONS:
        assert required_fields.issubset(
            dimension.keys()
        )


def test_dimension_ids_are_unique():
    dimension_ids = [
        dimension["id"]
        for dimension in HJPI_DIMENSIONS
    ]

    assert len(dimension_ids) == len(
        set(dimension_ids)
    )


def test_every_dimension_has_indicators():
    for dimension in HJPI_DIMENSIONS:
        assert len(dimension["indicators"]) > 0


def test_every_dimension_has_evidence_examples():
    for dimension in HJPI_DIMENSIONS:
        assert len(
            dimension["evidence_examples"]
        ) > 0


def test_maximum_total_score_matches_methodology():
    expected_maximum = (
        len(HJPI_DIMENSIONS)
        * MAX_DIMENSION_SCORE
    )

    assert (
        get_maximum_total_score()
        == expected_maximum
    )