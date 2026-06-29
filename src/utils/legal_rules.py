"""
=========================================================
LexiGuard AI
Legal Knowledge Base
=========================================================

This file contains the legal intelligence used by
ContractAnalyzer.

Each clause contains:

1. Detection keywords
2. Risk level
3. Description
4. Recommendation
5. Importance Score

=========================================================
"""

CLAUSE_DATABASE = {

    "Termination Clause": {

        "keywords": [
            "terminate",
            "termination",
            "terminated",
            "notice period",
            "end of agreement",
            "employment ends",
            "resignation",
            "dismissal"
        ],

        "risk": "Medium",

        "importance": 10,

        "description":
            "Defines how either party may legally terminate the agreement.",

        "recommendation":
            "Specify notice period, termination conditions, resignation process, severance obligations and termination for cause."

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

        "importance": 8,

        "description":
            "Protects confidential company information from unauthorized disclosure.",

        "recommendation":
            "Define confidential information, confidentiality duration and permitted disclosures."

    },

    "Payment Clause": {

        "keywords": [
            "payment",
            "invoice",
            "salary",
            "compensation",
            "fee",
            "billing",
            "remuneration",
            "bonus",
            "allowance"
        ],

        "risk": "Low",

        "importance": 9,

        "description":
            "Defines financial obligations between the parties.",

        "recommendation":
            "Clearly specify payment amount, payment schedule, penalties and reimbursement terms."

    },

    "Liability Clause": {

        "keywords": [
            "liability",
            "liable",
            "damages",
            "indemnify",
            "indemnification",
            "losses",
            "claims"
        ],

        "risk": "High",

        "importance": 10,

        "description":
            "Determines legal responsibility for damages and financial losses.",

        "recommendation":
            "Clearly define liability limits, exclusions and indemnification obligations."

    },

    "Warranty Clause": {

        "keywords": [
            "warranty",
            "guarantee",
            "merchantability",
            "fitness for purpose"
        ],

        "risk": "Medium",

        "importance": 7,

        "description":
            "Specifies guarantees regarding products, services or employment obligations.",

        "recommendation":
            "Define warranty duration, limitations and exclusions."

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

        "importance": 7,

        "description":
            "Explains how disputes between parties will be resolved.",

        "recommendation":
            "Specify arbitration rules, location, governing institution and appeal process."

    },

    "Force Majeure Clause": {

        "keywords": [
            "force majeure",
            "act of god",
            "pandemic",
            "earthquake",
            "war",
            "natural disaster"
        ],

        "risk": "Low",

        "importance": 8,

        "description":
            "Protects parties from liability during extraordinary unforeseen events.",

        "recommendation":
            "Clearly define qualifying events and notification requirements."

    },

    "Governing Law Clause": {

        "keywords": [
            "governing law",
            "jurisdiction",
            "applicable law",
            "court of law"
        ],

        "risk": "Low",

        "importance": 8,

        "description":
            "Specifies which country's or state's laws govern the agreement.",

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

        "importance": 9,

        "description":
            "Defines ownership of inventions, code, documents and creative work.",

        "recommendation":
            "Clarify ownership of work products and licensing rights."

    },

    "Data Privacy Clause": {

        "keywords": [
            "data privacy",
            "personal data",
            "gdpr",
            "privacy policy",
            "data protection",
            "sensitive information"
        ],

        "risk": "Medium",

        "importance": 8,

        "description":
            "Explains how personal or sensitive information will be collected and protected.",

        "recommendation":
            "Include compliance with GDPR, CCPA or applicable privacy regulations."

    },

    "Non-Compete Clause": {

        "keywords": [
            "non compete",
            "non-compete",
            "competitive business",
            "restrictive covenant"
        ],

        "risk": "Medium",

        "importance": 7,

        "description":
            "Restricts employees from working for competitors after employment.",

        "recommendation":
            "Specify duration, geographical scope and business limitations."

    },

    "Non-Solicitation Clause": {

        "keywords": [
            "non solicitation",
            "non-solicitation",
            "solicit employees",
            "solicit customers"
        ],

        "risk": "Low",

        "importance": 6,

        "description":
            "Prevents parties from soliciting employees or customers.",

        "recommendation":
            "Clearly define restricted activities and duration."

    }

}


# ============================================================
# Required Clauses
# ============================================================

REQUIRED_CLAUSES = [

    "Termination Clause",

    "Confidentiality Clause",

    "Payment Clause",

    "Liability Clause",

    "Governing Law Clause",

    "Force Majeure Clause",

    "Data Privacy Clause"

]


# ============================================================
# Risk Scoring
# ============================================================

RISK_SCORE = {

    "Low": 5,

    "Medium": 10,

    "High": 20

}


# ============================================================
# Overall Verdict Thresholds
# ============================================================

VERDICTS = {

    "Excellent": (90, 100),

    "Good": (75, 89),

    "Needs Review": (50, 74),

    "High Risk": (0, 49)

}