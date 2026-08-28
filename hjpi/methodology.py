
HJPI_DIMENSIONS = [
    {
        "id": "reasoning_transparency",
        "icon": "🔍",
        "name": "Reasoning Transparency",
        "description": (
            "Examines whether users have enough information to critically "
            "evaluate the basis of an AI-generated output."
        ),
        "screening_question": (
            "Does the AI system provide enough information for users to "
            "critically evaluate its outputs rather than simply accept them?"
        ),
        "indicators": [
            "Users can identify the main basis, evidence, or factors behind an output.",
            "The system communicates important uncertainty and limitations.",
            "Relevant supporting information or sources can be inspected where appropriate.",
            "Explanations are meaningful to the user rather than merely technically available.",
        ],
        "evidence_examples": [
            "System documentation",
            "Interface screenshots",
            "Explanation features",
            "User interviews",
            "Policies or guidance",
        ],
    },
    {
        "id": "user_override_capability",
        "icon": "🎛️",
        "name": "User Override Capability",
        "description": (
            "Examines whether users can meaningfully disagree with, modify, "
            "or reject AI-generated recommendations."
        ),
        "screening_question": (
            "Can users meaningfully reject, modify, or override the AI system's "
            "output when their judgment differs?"
        ),
        "indicators": [
            "Users can reject or modify an AI recommendation before it affects the final decision.",
            "Overriding the system does not involve unreasonable friction or penalty.",
            "Users have sufficient authority and time to intervene meaningfully.",
            "There is evidence that users actually exercise override when appropriate.",
        ],
        "evidence_examples": [
            "Workflow documentation",
            "Interface controls",
            "Override logs",
            "User interviews",
            "Organisational policies",
        ],
    },
    {
        "id": "skill_development",
        "icon": "📈",
        "name": "Skill Development",
        "description": (
            "Examines whether continued AI use preserves or develops relevant "
            "human capability rather than creating avoidable dependency."
        ),
        "screening_question": (
            "Does regular use of the AI system preserve or strengthen the "
            "skills users need to exercise independent judgment?"
        ),
        "indicators": [
            "The system encourages active reasoning rather than passive acceptance.",
            "Users retain the ability to perform or evaluate important aspects of the task independently.",
            "Training or feedback helps maintain relevant human expertise.",
            "The organisation considers or monitors dependency and potential deskilling.",
        ],
        "evidence_examples": [
            "Training materials",
            "User interviews",
            "Performance observations",
            "Skills assessments",
            "Usage studies",
        ],
    },
    {
        "id": "no_decision_outsourcing",
        "icon": "🧠",
        "name": "No Decision Outsourcing",
        "description": (
            "Examines whether humans continue to exercise meaningful judgment "
            "rather than merely approving AI-generated recommendations."
        ),
        "screening_question": (
            "Are users genuinely evaluating AI outputs and making the final "
            "judgment rather than routinely accepting the system's recommendation?"
        ),
        "indicators": [
            "Human responsibility for important decisions is clearly assigned.",
            "Users independently evaluate AI outputs before acting on them.",
            "The workflow does not make acceptance of the AI recommendation the automatic default.",
            "Human reasoning or justification remains visible in important decisions.",
        ],
        "evidence_examples": [
            "Decision records",
            "Workflow procedures",
            "Approval processes",
            "User interviews",
            "Usage or acceptance data",
        ],
    },
    {
        "id": "transparency_at_use",
        "icon": "💡",
        "name": "Transparency at Use",
        "description": (
            "Examines whether users understand that AI is involved, what role "
            "it plays, and the limits of appropriate reliance on it."
        ),
        "screening_question": (
            "Do users understand that AI is involved, what role it plays, "
            "and the limits of appropriate reliance on its outputs?"
        ),
        "indicators": [
            "Users know when they are interacting with or receiving output from an AI system.",
            "The role of the AI within the wider decision process is clearly communicated.",
            "Important limitations and appropriate-use conditions are communicated.",
            "Relevant users understand when human review or escalation is required.",
        ],
        "evidence_examples": [
            "User interface",
            "Disclosure notices",
            "Training materials",
            "Policies",
            "User interviews",
        ],
    },
    {
        "id": "judgment_shaping",
        "icon": "🧭",
        "name": "Judgment Shaping & Choice Architecture",
        "description": (
            "Examines whether an AI system shapes how users frame a problem, "
            "perceive available options, weigh information, or form preferences "
            "in ways that may materially influence their judgment."
        ),
        "screening_question": (
            "Does the AI system shape which options, evidence, or interpretations "
            "users consider in ways that could materially influence their judgment?"
        ),
        "indicators": [
            "The system does not unnecessarily restrict which options or alternatives users can consider.",
            "The framing or wording of AI outputs does not unduly privilege one interpretation or course of action.",
            "Important evidence and considerations are not selectively emphasized or omitted in ways that distort judgment.",
            "Users can meaningfully explore alternatives beyond those initially suggested by the AI system.",
            "Defaults or recommended actions do not create inappropriate pressure toward a particular decision.",
            "Personalization does not exploit user characteristics to exert inappropriate persuasive influence.",
            "Users can recognize when the presentation of information may itself be influencing their judgment.",
        ],
        "evidence_examples": [
            "AI-generated recommendations",
            "Prompt and response samples",
            "User interface screenshots",
            "Recommendation-ranking logic",
            "Personalization documentation",
            "User interviews",
            "Decision workflow documentation",
        ],
    },
]


DIMENSIONS = [
    dimension["name"]
    for dimension in HJPI_DIMENSIONS
]


CONFIDENCE_LEVELS = [
    "Low",
    "Medium",
    "High",
]