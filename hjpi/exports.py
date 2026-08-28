
import csv
from datetime import datetime
from io import BytesIO, StringIO

from hjpi.methodology import DIMENSIONS


def create_csv_export(
    meta,
    scores,
    total,
    percentage,
    verdict,
):
    """Create a downloadable CSV representation of an HJPI assessment."""

    if len(scores) != len(DIMENSIONS):
        raise ValueError(
            "The number of scores must match the number of HJPI dimensions."
        )

    row = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "System Name": meta["system_name"],
        "Evaluator": meta["evaluator"],
        "Organisation": meta["organisation"],
        "Context": meta["context"],
    }

    for i, (dimension, score) in enumerate(
        zip(DIMENSIONS, scores),
        start=1,
    ):
        row[f"Q{i} {dimension}"] = score

    row["Total"] = total
    row["Percentage"] = round(percentage, 1)
    row["Verdict"] = verdict

    output = StringIO()

    writer = csv.DictWriter(
        output,
        fieldnames=row.keys(),
    )

    writer.writeheader()
    writer.writerow(row)

    return output.getvalue().encode("utf-8")


def create_png_export(fig):
    """Convert an HJPI matplotlib figure into downloadable PNG bytes."""

    buffer = BytesIO()

    fig.savefig(
        buffer,
        format="png",
        dpi=150,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )

    buffer.seek(0)

    return buffer.getvalue()