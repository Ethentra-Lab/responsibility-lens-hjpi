# ============================================================
# The Responsibility Lens | Human Judgment Preservation Index
# By Aderayo Adelanwa | ETHENTRA
# ============================================================


import streamlit as st

from hjpi.charts import create_radar_chart
from hjpi.config import (
    MAX_DIMENSION_SCORE,
    get_maximum_total_score,
)
from hjpi.exports import create_csv_export, create_png_export
from hjpi.methodology import HJPI_DIMENSIONS, DIMENSIONS
from hjpi.scoring import calculate_score, get_verdict


# ============================================================
# PRIVATE SCORING CONFIGURATION
# ============================================================

THRESHOLDS = {
    "pass": st.secrets["thresholds"]["pass"],
    "conditional": st.secrets["thresholds"]["conditional"],
    "redesign": st.secrets["thresholds"]["redesign"],
}

VERDICT_LABELS = dict(st.secrets["verdict_labels"])
VERDICT_MESSAGES = dict(st.secrets["verdict_messages"])


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HJPI Tool | The Responsibility Lens",
    page_icon="🔍",
    layout="centered",
)


# ============================================================
# BRAND STYLING
# ============================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

.brand-header {
    background: #1A1A1A;
    color: #F2E8DE;
    padding: 2rem 2.5rem;
    border-radius: 4px;
    margin-bottom: 2rem;
}

.brand-header h1 {
    color: #F2E8DE;
    font-size: 1.8rem;
    margin: 0 0 0.3rem 0;
}

.brand-header p {
    color: #FF4810;
    font-size: 0.9rem;
    margin: 0;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.section-label {
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #FF4810;
    font-weight: 500;
    margin-bottom: 0.3rem;
}

.verdict-box {
    padding: 1.5rem 2rem;
    border-radius: 4px;
    margin: 1.5rem 0;
    border-left: 5px solid;
}

.verdict-pass {
    background: #F0F7F0;
    border-color: #2D7A2D;
    color: #1A3D1A;
}

.verdict-conditional {
    background: #FFF8EC;
    border-color: #C97D00;
    color: #3D2800;
}

.verdict-redesign {
    background: #FFF3EC;
    border-color: #B5622A;
    color: #3D1500;
}

.verdict-fail {
    background: #FFF0F0;
    border-color: #C0392B;
    color: #3D0000;
}

.score-summary {
    display: flex;
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.score-card {
    background: #1A1A1A;
    color: #F2E8DE;
    padding: 1rem 1.5rem;
    border-radius: 4px;
    text-align: center;
    flex: 1;
}

.score-card .number {
    font-size: 2rem;
    color: #FF4810;
}

.score-card .label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    opacity: 0.7;
}

.footer {
    text-align: center;
    color: #7A6A5E;
    font-size: 0.8rem;
    padding: 2rem 0 1rem 0;
    border-top: 1px solid #DDD0C4;
    margin-top: 3rem;
}

.stButton > button {
    background: #FF4810 !important;
    color: #F2E8DE !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 500 !important;
    width: 100%;
}

.stButton > button:hover {
    background: #B5622A !important;
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_verdict_message(level):
    return VERDICT_MESSAGES[level]


# ============================================================
# SESSION STATE
# ============================================================

if "step" not in st.session_state:
    st.session_state.step = "intro"


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
<div class="brand-header">
    <h1>The Responsibility Lens</h1>
    <p>Human Judgment Preservation Index · ETHENTRA</p>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# INTRO
# ============================================================

if st.session_state.step == "intro":
    st.markdown("### What is the HJPI Tool?")

    st.markdown(
        f"""
The **Human Judgment Preservation Index (HJPI)** is a structured screening
assessment for examining how an AI-assisted system may affect human judgment,
agency, and meaningful oversight.

It evaluates the system across **{len(HJPI_DIMENSIONS)} dimensions** and
identifies potential risks to the preservation of human judgment,
highlighting areas that may require deeper review.
"""
    )

    st.markdown("---")

    st.markdown(
        f'<div class="section-label">'
        f'The {len(HJPI_DIMENSIONS)} Dimensions'
        f'</div>',
        unsafe_allow_html=True,
    )

    for dimension in HJPI_DIMENSIONS:
        st.markdown(
            f"**{dimension['icon']} {dimension['name']}** — "
            f"{dimension['description']}"
        )

    st.markdown("---")

    if st.button("Begin Evaluation →"):
        st.session_state.step = "details"
        st.rerun()


# ============================================================
# SYSTEM DETAILS
# ============================================================

elif st.session_state.step == "details":
    st.markdown("### Step 1 of 2 — System Details")

    st.markdown(
        '<div class="section-label">'
        'Tell us about the AI system you are evaluating'
        '</div>',
        unsafe_allow_html=True,
    )

    with st.form("details_form"):
        system_name = st.text_input(
            "AI System / Product Name *"
        )

        evaluator = st.text_input(
            "Your Name *"
        )

        organisation = st.text_input(
            "Organisation *"
        )

        context = st.text_area(
            "Your role and reason for this evaluation",
            height=80,
        )

        submitted = st.form_submit_button(
            "Continue to Scoring →"
        )

        if submitted:
            if not system_name or not evaluator or not organisation:
                st.error(
                    "Please complete all required fields (*)."
                )

            else:
                st.session_state.meta = {
                    "system_name": system_name,
                    "evaluator": evaluator,
                    "organisation": organisation,
                    "context": context,
                }

                st.session_state.step = "scoring"
                st.rerun()


# ============================================================
# SCORING
# ============================================================

elif st.session_state.step == "scoring":
    st.markdown("### Step 2 of 2 — Dimension Scoring")

    st.markdown(
        f'<div class="section-label">'
        f'Evaluating: {st.session_state.meta["system_name"]}'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        "Rate each dimension from "
        "**1 (Very Poor)** to **5 (Excellent)**."
    )

    st.markdown("---")

    score_options = {
        "1 — Very Poor": 1,
        "2 — Poor": 2,
        "3 — Moderate": 3,
        "4 — Good": 4,
        "5 — Excellent": 5,
    }

    with st.form("scoring_form"):
        scores = []

        for i, dimension in enumerate(HJPI_DIMENSIONS):
            st.markdown(
                f"**Q{i + 1}. "
                f"{dimension['icon']} "
                f"{dimension['name']}**"
            )

            st.caption(
                dimension["screening_question"]
            )

            with st.expander(
                "What a deeper review would examine"
            ):
                for indicator in dimension["indicators"]:
                    st.markdown(
                        f"- {indicator}"
                    )

            choice = st.radio(
                f"score_{i}",
                options=list(score_options.keys()),
                index=2,
                horizontal=True,
                label_visibility="collapsed",
                key=f"q{i}",
            )

            scores.append(
                score_options[choice]
            )

            if i < len(HJPI_DIMENSIONS) - 1:
                st.markdown("---")

        submitted = st.form_submit_button(
            "Generate Results →"
        )

        if submitted:
            st.session_state.scores = scores
            st.session_state.step = "results"
            st.rerun()

# ============================================================
# RESULTS
# ============================================================

elif st.session_state.step == "results":
    scores = st.session_state.scores
    meta = st.session_state.meta

    total, percentage = calculate_score(scores)

    verdict, level = get_verdict(
        percentage,
        THRESHOLDS,
        VERDICT_LABELS,
    )

    maximum_score = get_maximum_total_score()

    verdict_class = {
        "PASS": "verdict-pass",
        "CONDITIONAL": "verdict-conditional",
        "REDESIGN": "verdict-redesign",
        "FAIL": "verdict-fail",
    }[level]

    st.markdown("### Evaluation Results")

    st.markdown(
        f'<div class="section-label">'
        f'{meta["system_name"]} · '
        f'{meta["organisation"]}'
        f'</div>',
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Score Summary
    # --------------------------------------------------------

    score_summary_html = (
        f'<div class="score-summary">'
        f'<div class="score-card">'
        f'<div class="number">{total}/{maximum_score}</div>'
        f'<div class="label">Total Score</div>'
        f'</div>'
        f'<div class="score-card">'
        f'<div class="number">{percentage:.1f}%</div>'
        f'<div class="label">HJPI Score</div>'
        f'</div>'
        f'</div>'
    )

    st.markdown(
        score_summary_html,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Verdict
    # --------------------------------------------------------

    verdict_html = (
        f'<div class="verdict-box {verdict_class}">'
        f'<strong>SCREENING VERDICT</strong><br>'
        f'<span style="font-size:1.1rem; font-weight:600">'
        f'{verdict}'
        f'</span>'
        f'<br><br>'
        f'{get_verdict_message(level)}'
        f'</div>'
    )

    st.markdown(
        verdict_html,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Dimension Breakdown
    # --------------------------------------------------------

    st.markdown("---")
    st.markdown("**Dimension Breakdown**")

    for dimension, score in zip(DIMENSIONS, scores):
        col1, col2, col3 = st.columns([3, 1, 1])

        col1.markdown(
            f"<small>{dimension}</small>",
            unsafe_allow_html=True,
        )

        col2.markdown(
            f"<small style='color:#FF4810'>"
            f"{'█' * score}"
            f"{'░' * (MAX_DIMENSION_SCORE - score)}"
            f"</small>",
            unsafe_allow_html=True,
        )

        col3.markdown(
            f"<small>"
            f"<b>{score}/{MAX_DIMENSION_SCORE}</b>"
            f"</small>",
            unsafe_allow_html=True,
        )

    # --------------------------------------------------------
    # Radar Chart
    # --------------------------------------------------------

    st.markdown("---")
    st.markdown("**HJPI Radar Chart**")

    fig = create_radar_chart(
        scores,
        meta["system_name"],
        total,
        percentage,
        verdict,
    )

    st.pyplot(fig)

    # --------------------------------------------------------
    # Downloads
    # --------------------------------------------------------

    st.markdown("---")
    st.markdown("**Download Results**")

    col1, col2 = st.columns(2)

    csv_data = create_csv_export(
        meta,
        scores,
        total,
        percentage,
        verdict,
    )

    col1.download_button(
        label="⬇ Download CSV",
        data=csv_data,
        file_name=(
            f"hjpi_"
            f"{meta['system_name'].replace(' ', '_')}.csv"
        ),
        mime="text/csv",
    )

    png_data = create_png_export(fig)

    col2.download_button(
        label="⬇ Download Chart",
        data=png_data,
        file_name=(
            f"hjpi_"
            f"{meta['system_name'].replace(' ', '_')}.png"
        ),
        mime="image/png",
    )

    # --------------------------------------------------------
    # Restart Assessment
    # --------------------------------------------------------

    st.markdown("---")

    if st.button("← Run Another Evaluation"):
        for key in [
            "step",
            "meta",
            "scores",
        ]:
            if key in st.session_state:
                del st.session_state[key]

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">
    The Responsibility Lens | ETHENTRA<br>
    hello@ethentra.co | https://ethentra.co/
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# PROFESSIONAL REVIEW CTA
# ============================================================

st.markdown("---")

review_cta_html = (
    '<div style="'
    'background:#FFF8EC;'
    'border-left:5px solid #FF4810;'
    'padding:1rem 1.5rem;'
    'border-radius:4px;'
    'margin-top:1rem;'
    '">'
    '<b style="color:#1A1A1A;">'
    '📋 Need a deeper Human Judgment Risk Review?'
    '</b>'
    '<br><br>'
    '<span style="color:#7A6A5E;">'
    'Explore a professional assessment of your AI system, '
    'evidence, human-judgment risks, and areas requiring deeper review.'
    '</span>'
    '<br><br>'
    '<a href="mailto:lab@ethentra.com" '
    'style="color:#FF4810; font-weight:600;">'
    'Contact ETHENTRA → lab@ethentra.co'
    '</a>'
    '</div>'
)

st.markdown(
    review_cta_html,
    unsafe_allow_html=True,
)