import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from hjpi.config import MAX_DIMENSION_SCORE, get_maximum_total_score
from hjpi.methodology import DIMENSIONS


def create_radar_chart(scores, system_name, total, percentage, verdict):
    if len(scores) != len(DIMENSIONS):
        raise ValueError(
            "The number of scores must match the number of HJPI dimensions."
        )

    radar_labels = [
        dimension.replace(" ", "\n", 1)
        for dimension in DIMENSIONS
    ]

    num_dims = len(DIMENSIONS)

    angles = np.linspace(
        0,
        2 * np.pi,
        num_dims,
        endpoint=False,
    ).tolist()

    scores_plot = scores + [scores[0]]
    angles += angles[:1]

    fig, ax = plt.subplots(
        figsize=(7, 7),
        subplot_kw=dict(polar=True),
    )

    fig.patch.set_facecolor("#F2E8DE")
    ax.set_facecolor("#F2E8DE")

    ax.fill(
        angles,
        scores_plot,
        color="#FF4810",
        alpha=0.25,
    )

    ax.plot(
        angles,
        scores_plot,
        color="#FF4810",
        linewidth=2.5,
    )

    for angle, score in zip(angles[:-1], scores):
        ax.plot(
            angle,
            score,
            "o",
            color="#FF4810",
            markersize=7,
            zorder=5,
        )

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(
        radar_labels,
        size=10,
        fontweight="bold",
        color="#1A1A1A",
    )

    ax.set_ylim(0, MAX_DIMENSION_SCORE)

    ax.set_yticks(
        range(1, MAX_DIMENSION_SCORE + 1)
    )

    ax.set_yticklabels(
        [
            str(score)
            for score in range(1, MAX_DIMENSION_SCORE + 1)
        ],
        size=8,
        color="#7A6A5E",
    )

    ax.grid(
        color="#DDD0C4",
        linestyle="--",
        linewidth=0.6,
    )

    ax.spines["polar"].set_color("#DDD0C4")

    maximum_score = get_maximum_total_score()

    plt.title(
        f"HJPI — {system_name}\n"
        f"{total}/{maximum_score}  "
        f"({percentage:.1f}%)  |  {verdict}",
        size=11,
        fontweight="bold",
        color="#1A1A1A",
        pad=20,
    )

    fig.text(
        0.5,
        0.01,
        "The Responsibility Lens | "
        "Ethentra Limited | hello@ethentra.co",
        ha="center",
        size=8,
        color="#7A6A5E",
    )

    return fig