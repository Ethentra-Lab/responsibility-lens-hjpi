import csv
from io import StringIO

import pytest

from hjpi.exports import create_csv_export
from hjpi.methodology import DIMENSIONS


def test_csv_export_contains_all_dimensions():
    meta = {
        "system_name": "Test AI",
        "evaluator": "Test Evaluator",
        "organisation": "Test Organisation",
        "context": "Testing",
    }

    scores = [5, 4, 3, 2, 1, 3]

    csv_bytes = create_csv_export(
        meta=meta,
        scores=scores,
        total=sum(scores),
        percentage=60.0,
        verdict="Test Verdict",
    )

    csv_text = csv_bytes.decode("utf-8")

    reader = csv.DictReader(
        StringIO(csv_text)
    )

    row = next(reader)

    for i, dimension in enumerate(
        DIMENSIONS,
        start=1,
    ):
        assert f"Q{i} {dimension}" in row


def test_csv_export_contains_metadata():
    meta = {
        "system_name": "Test AI",
        "evaluator": "Test Evaluator",
        "organisation": "Test Organisation",
        "context": "Testing context",
    }

    scores = [5, 4, 3, 2, 1, 3]

    csv_bytes = create_csv_export(
        meta=meta,
        scores=scores,
        total=sum(scores),
        percentage=60.0,
        verdict="Test Verdict",
    )

    csv_text = csv_bytes.decode("utf-8")

    reader = csv.DictReader(
        StringIO(csv_text)
    )

    row = next(reader)

    assert row["System Name"] == "Test AI"
    assert row["Evaluator"] == "Test Evaluator"
    assert row["Organisation"] == "Test Organisation"
    assert row["Context"] == "Testing context"


def test_csv_export_rejects_wrong_number_of_scores():
    meta = {
        "system_name": "Test AI",
        "evaluator": "Test Evaluator",
        "organisation": "Test Organisation",
        "context": "Testing",
    }

    with pytest.raises(ValueError):
        create_csv_export(
            meta=meta,
            scores=[5, 4],
            total=9,
            percentage=90.0,
            verdict="Test Verdict",
        )