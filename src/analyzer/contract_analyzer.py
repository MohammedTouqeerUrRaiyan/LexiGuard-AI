from src.utils.legal_rules import (
    CLAUSE_DATABASE,
    REQUIRED_CLAUSES,
    RISK_SCORE,
    IMPORTANCE_PENALTY,
    VERDICTS
)


class ContractAnalyzer:

    def __init__(self):
        self.clauses = CLAUSE_DATABASE

    # --------------------------------------------------
    # Detect Clauses
    # --------------------------------------------------

    def detect_clauses(self, text):

        processed = text.lower()

        detected = []
        keywords_found = []
        clause_details = []

        total_risk_score = 0

        for clause_name, info in self.clauses.items():

            matched_keywords = []

            for keyword in info["keywords"]:

                if keyword.lower() in processed:
                    matched_keywords.append(keyword)

            if matched_keywords:

                detected.append(clause_name)

                keywords_found.extend(matched_keywords)

                total_risk_score += RISK_SCORE[info["risk"]]

                clause_details.append({

                    "clause": clause_name,

                    "risk": info["risk"],

                    "importance": info["importance"],

                    "matched_keywords": matched_keywords,

                    "description": info["description"],

                    "recommendation": info["recommendation"]

                })
                

        return (
            detected,
            list(set(keywords_found)),
            clause_details,
            total_risk_score
        )

    # --------------------------------------------------
    # Missing Clauses
    # --------------------------------------------------

    def detect_missing_clauses(self, detected):

        missing = []

        for clause in REQUIRED_CLAUSES:

            if clause not in detected:

                info = self.clauses[clause]

                missing.append({

                    "clause": clause,

                    "importance": info["importance"],

                    "description": info["description"],

                    "recommendation": info["recommendation"]

                })

        return missing

    # --------------------------------------------------
    # Risk
    # --------------------------------------------------

    def calculate_risk(self, score):

        if score >= 40:
            return "High"

        if score >= 20:
            return "Medium"

        return "Low"

    # --------------------------------------------------
    # Contract Health
    # --------------------------------------------------

    def calculate_health(self, missing, risk):

        health = 100

        for clause in missing:

            health -= IMPORTANCE_PENALTY[clause["importance"]]

        if risk == "Medium":
            health -= 10

        elif risk == "High":
            health -= 20

        return max(0, min(100, health))

    # --------------------------------------------------
    # Verdict
    # --------------------------------------------------

    def generate_verdict(self, health):

        for verdict, (low, high) in VERDICTS.items():

            if low <= health <= high:
                return verdict

        return "Needs Review"

    # --------------------------------------------------
    # Executive Summary
    # --------------------------------------------------

    def generate_summary(

        self,
        detected,
        missing,
        risk,
        verdict

    ):

        summary = (
            f"The contract contains {len(detected)} recognised legal clauses "
            f"and is missing {len(missing)} recommended clauses. "
            f"The overall legal risk is assessed as {risk}. "
            f"Overall contract quality is rated '{verdict}'."
        )

        return summary

    # --------------------------------------------------
    # Warnings
    # --------------------------------------------------

    def generate_warnings(self, detected):

        warnings = []

        if "Liability Clause" in detected:

            warnings.append(
                "Review liability obligations carefully. They may expose one party to significant financial responsibility."
            )

        if "Termination Clause" in detected:

            warnings.append(
                "Verify termination conditions and notice period."
            )

        if "Payment Clause" in detected:

            warnings.append(
                "Verify payment schedule, penalties and reimbursement terms."
            )

        if "Confidentiality Clause" in detected:

            warnings.append(
                "Ensure confidentiality obligations continue after contract termination."
            )

        return warnings

    # --------------------------------------------------
    # Overall Recommendations
    # --------------------------------------------------

    def overall_recommendations(self, missing):

        recommendations = []

        for clause in missing:

            recommendations.append(
                f"Add a {clause['clause']}."
            )

        if not recommendations:
            recommendations.append(
                "No major contractual weaknesses detected."
            )

        return recommendations

    # --------------------------------------------------
    # Main Analysis
    # --------------------------------------------------

    def analyze(self, text):

        (
            detected,
            keywords,
            clause_details,
            risk_score

        ) = self.detect_clauses(text)

        missing = self.detect_missing_clauses(detected)

        risk = self.calculate_risk(risk_score)

        health = self.calculate_health(
            missing,
            risk
        )

        verdict = self.generate_verdict(health)

        summary = self.generate_summary(
            detected,
            missing,
            risk,
            verdict
        )

        warnings = self.generate_warnings(detected)

        recommendations = self.overall_recommendations(
            missing
        )

        return {

            "document": {

                "word_count": len(text.split()),

                "character_count": len(text)

            },

            "analysis": {

                "risk_level": risk,

                "contract_health": health,

                "contract_score": health,

                "verdict": verdict,

                "summary": summary

            },

            "statistics": {

                "detected_clauses": len(detected),

                "missing_clauses": len(missing),

                "keywords_found": len(keywords)

            },

            "clauses": {

                "detected": clause_details,

                "missing": missing

            },

            "keywords_found": keywords,

            "warnings": warnings,

            "overall_recommendations": recommendations

        }
    # --------------------------------------------------
    # Risk Factors
    # --------------------------------------------------

    def generate_risk_factors(self, detected_clauses):

        factors = []

        high_risk = {
            "Liability Clause",
            "Termination Clause",
            "Intellectual Property Clause",
            "Data Privacy Clause",
            "Non-Compete Clause"
        }

        for clause in detected_clauses:
            if clause in high_risk:
                factors.append(clause)

        return factors