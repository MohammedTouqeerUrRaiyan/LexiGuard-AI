"""
=========================================================
LexiGuard AI
Legal Knowledge Base
=========================================================

This module acts as the central legal intelligence layer.

Every legal clause contains:

• Detection keywords
• Risk category
• Importance level
• Description
• Recommendation

Nothing outside this file should hardcode legal rules.
"""

# ==========================================================
# Contract Clause Database
# ==========================================================

CLAUSE_DATABASE = {

    "Termination Clause": {

        "keywords": [
            "terminate",
            "termination",
            "terminated",
            "notice period",
            "end of agreement",
            "dismissal",
            "resignation"
        ],

        "risk": "Medium",

        "importance": "High",

        "description":
        "Defines how either party may legally terminate the agreement.",

        "recommendation":
        "Clearly define notice period, termination for cause, resignation process and severance obligations."

    },

    "Confidentiality Clause": {

        "keywords": [
            "confidential",
            "confidentiality",
            "nda",
            "non-disclosure",
            "trade secret",
            "proprietary information"
        ],

        "risk": "Low",

        "importance": "High",

        "description":
        "Protects confidential information from unauthorized disclosure.",

        "recommendation":
        "Specify confidential information, confidentiality duration and permitted disclosures."

    },

    "Payment Clause": {

        "keywords": [
            "payment",
            "salary",
            "invoice",
            "billing",
            "fee",
            "compensation",
            "bonus",
            "allowance",
            "remuneration"
        ],

        "risk": "Low",

        "importance": "High",

        "description":
        "Defines financial obligations between parties.",

        "recommendation":
        "Clearly specify payment amount, due dates, penalties and reimbursement terms."

    },

    "Liability Clause": {

        "keywords": [
            "liability",
            "liable",
            "indemnify",
            "indemnification",
            "damages",
            "losses",
            "claims"
        ],

        "risk": "High",

        "importance": "High",

        "description":
        "Determines legal responsibility for losses or damages.",

        "recommendation":
        "Clearly define liability limits, exclusions and indemnification responsibilities."

    },

    "Warranty Clause": {

        "keywords": [
            "warranty",
            "guarantee",
            "merchantability",
            "fitness for purpose"
        ],

        "risk": "Medium",

        "importance": "Medium",

        "description":
        "Defines warranties or guarantees regarding products or services.",

        "recommendation":
        "Clearly define warranty duration, exclusions and claim procedures."

    },

    "Arbitration Clause": {

        "keywords": [
            "arbitration",
            "dispute resolution",
            "mediator",
            "arbitrator",
            "settlement"
        ],

        "risk": "Low",

        "importance": "Medium",

        "description":
        "Specifies how legal disputes will be resolved.",

        "recommendation":
        "Specify arbitration rules, institution, governing law and venue."

    },

    "Force Majeure Clause": {

        "keywords": [
            "force majeure",
            "natural disaster",
            "pandemic",
            "earthquake",
            "war",
            "act of god"
        ],

        "risk": "Low",

        "importance": "High",

        "description":
        "Protects parties from liability during extraordinary unforeseen events.",

        "recommendation":
        "Clearly define qualifying events and notification procedures."

    },

    "Governing Law Clause": {

        "keywords": [
            "governing law",
            "jurisdiction",
            "court of law",
            "applicable law"
        ],

        "risk": "Low",

        "importance": "High",

        "description":
        "Specifies which jurisdiction governs the contract.",

        "recommendation":
        "Clearly identify governing jurisdiction and legal venue."

    },

    "Intellectual Property Clause": {

        "keywords": [
            "intellectual property",
            "copyright",
            "patent",
            "trademark",
            "ownership",
            "source code"
        ],

        "risk": "Medium",

        "importance": "Medium",

        "description":
        "Defines ownership of inventions, software and creative work.",

        "recommendation":
        "Clarify ownership rights, licensing and future usage."

    },

    "Data Privacy Clause": {

        "keywords": [
            "gdpr",
            "ccpa",
            "privacy",
            "personal data",
            "data protection",
            "sensitive information"
        ],

        "risk": "Medium",

        "importance": "High",

        "description":
        "Explains how personal information is collected and protected.",

        "recommendation":
        "Include compliance with GDPR, CCPA and applicable privacy regulations."

    },

    "Non-Compete Clause": {

        "keywords": [
            "non compete",
            "non-compete",
            "competitive business",
            "restrictive covenant"
        ],

        "risk": "Medium",

        "importance": "Medium",

        "description":
        "Restricts employees from joining competitors.",

        "recommendation":
        "Clearly specify geographical scope and duration."

    },

    "Non-Solicitation Clause": {

        "keywords": [
            "non solicitation",
            "non-solicitation",
            "solicit customers",
            "solicit employees"
        ],

        "risk": "Low",

        "importance": "Low",

        "description":
        "Restricts solicitation of employees or customers.",

        "recommendation":
        "Define restricted activities and applicable duration."

    }

}

# ==========================================================
# Required Clauses
# ==========================================================

REQUIRED_CLAUSES = [

    "Termination Clause",

    "Confidentiality Clause",

    "Payment Clause",

    "Liability Clause",

    "Force Majeure Clause",

    "Governing Law Clause",

    "Data Privacy Clause"

]

# ==========================================================
# Numerical Risk Scores
# ==========================================================

RISK_SCORE = {

    "Low": 5,

    "Medium": 10,

    "High": 20

}

# ==========================================================
# Importance Penalties
# ==========================================================

IMPORTANCE_PENALTY = {

    "High": 15,

    "Medium": 8,

    "Low": 4

}

# ==========================================================
# Overall Contract Grades
# ==========================================================

VERDICTS = {

    "Excellent": (90, 100),

    "Good": (75, 89),

    "Needs Review": (60, 74),

    "High Risk": (40, 59),

    "Critical": (0, 39)

}