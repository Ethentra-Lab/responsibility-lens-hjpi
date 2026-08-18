# The Responsibility Lens — HJPI Scoring Tool
**Human Judgment Preservation Index**  
By Aderayo Adelanwa | Ethentra 

---

## What is the HJPI Tool?

The **Human Judgment Preservation Index (HJPI)** evaluates whether an AI system supports or erodes human judgment over time.

It scores any AI system across five dimensions and returns a **Flourishing Verdict** — telling you whether the system is safe to deploy, needs redesign, or should be rejected.

Built for AI practitioners, ethics reviewers, and B2B tech teams who need a structured way to assess AI systems before deployment.

## Free Tool vs. Full Audit

The Responsibility Lens (this tool) provides a self-assessment score for individual use.

For a complete mixed-methods audit — including qualitative analysis, risk review, and strategic recommendations for your organization — see the **HJPI Full Audit** at [ethentra.co](https://ethentra.co).

## The Five Dimensions

| # | Dimension | Question |
|---|-----------|----------|
| 1 | Reasoning Transparency | Does the AI show its reasoning so users can evaluate the logic? |
| 2 | User Override Capability | Can users override the system — and do they actually use it? |
| 3 | Skill Development | Does regular use build user skills rather than dependency? |
| 4 | No Decision Outsourcing | Are users genuinely reviewing outputs, not just approving them? |
| 5 | Transparency at Use | Do users understand what the system does at point of use? |




## Versions

* V1 — Scoring tool with CSV saving ✅
* V2 — Radar chart visualisation ✅
* V3 — Streamlit web interface ✅

---

## How to Run

### Web Interface (V3) — Recommended

Try it live: https://responsibility-lens-hjpi.streamlit.app/

To run locally (requires a `scoring_config.py` file, not included in this
public repo — contact lab@ethentra.com for access):

​```bash
pip install streamlit matplotlib numpy
streamlit run hjpi_app.py
​```
### Streamlit Version
```bash
https://responsibility-lens-hjpi.streamlit.app/
```

### Terminal Version (V1/V2)
```bash
python hjpi_tool.py
```


## Output

* Interactive scoring across five dimensions
* Flourishing Verdict — Pass, Conditional, Redesign, or Fail
* Radar chart visualisation
* Downloadable CSV result
* Downloadable PNG chart


## Requirements

```
streamlit
matplotlib
numpy
```

Install all at once:
```bash
pip install streamlit matplotlib numpy
```

## About


**Ethentra** is a research-driven technology strategy and design firm operating at the intersection of ethics, design, and technology. We help founders, organizations, institutions, and technology teams make better decisions about consequential digital and AI systems. Our work combines research, strategic thinking, UX and interaction design, AI ethics, product strategy, and technical understanding to examine what should be built, how it should work, and what risks or unintended consequences need to be addressed.

Our flagship offering, the **HJPI Full Audit**, applies this approach directly to AI products and features — see [ethentra.co](https://ethentra.co) for details.

## Usage

This tool is free to use for self-assessment and educational purposes.

The HJPI methodology, scoring weights, and verdict thresholds are proprietary to Ethentra and may not be reproduced, redistributed, or used commercially without permission.

For commercial, enterprise, or partnership use, contact lab@ethentra.com.

- 🌐 https://ethentra.co
- 📧 Contact & Partnerships: lab@ethentra.com



*The **Human Judgment Preservation Index (HJPI)** is part of Ethentra's Human-Centered AI toolkit.*
© Ethentra. All rights reserved.
