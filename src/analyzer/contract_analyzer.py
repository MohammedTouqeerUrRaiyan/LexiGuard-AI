from src.embeddings.semantic_search import SemanticSearch
from src.clause_classifier.classifier import ClauseClassifier
from src.utils.legal_rules import (
    IMPORTANCE_PENALTY,
    RISK_SCORE,
    VERDICTS
)


class ContractAnalyzer:

    def __init__(self):

        self.classifier = ClauseClassifier()

        #self.semantic_search = SemanticSearch()

    # -------------------------------------------------------
    # Risk Score
    # -------------------------------------------------------

    def calculate_risk(self, detected):

        score = 0

        risk_factors = []

        for clause in detected:

            score += RISK_SCORE[clause["risk"]]

            if clause["risk"] in ["High", "Medium"]:
                risk_factors.append(clause["clause"])

        if score >= 40:
            risk = "High"

        elif score >= 20:
            risk = "Medium"

        else:
            risk = "Low"

        return risk, score, risk_factors

    # -------------------------------------------------------
    # Contract Health
    # -------------------------------------------------------

    def calculate_health(self, missing, risk):

        health = 100

        for clause in missing:

            health -= IMPORTANCE_PENALTY[clause["importance"]]

        if risk == "Medium":
            health -= 10

        elif risk == "High":
            health -= 20

        return max(0, min(100, health))

    # -------------------------------------------------------
    # Verdict
    # -------------------------------------------------------

    def generate_verdict(self, health):

        for verdict, (low, high) in VERDICTS.items():

            if low <= health <= high:
                return verdict

        return "Needs Review"

    # -------------------------------------------------------
    # Executive Summary
    # -------------------------------------------------------

    def generate_summary(self, detected, missing, risk, verdict):

        return (
            f"The contract contains {len(detected)} recognised legal clauses. "
            f"{len(missing)} important clauses are missing. "
            f"The overall legal risk is {risk}. "
            f"Final assessment: {verdict}."
        )

    # -------------------------------------------------------
    # Warnings
    # -------------------------------------------------------

    def generate_warnings(self, detected):

        warnings = []

        detected_names = {

            clause["clause"]

            for clause in detected

        }

        if "Liability Clause" in detected_names:

            warnings.append(
                "Review liability obligations carefully."
            )

        if "Termination Clause" in detected_names:

            warnings.append(
                "Verify termination conditions and notice period."
            )

        if "Payment Clause" in detected_names:

            warnings.append(
                "Verify payment schedules and penalties."
            )

        if "Confidentiality Clause" in detected_names:

            warnings.append(
                "Ensure confidentiality survives contract termination."
            )

        return warnings

    # -------------------------------------------------------
    # Recommendations
    # -------------------------------------------------------

    def generate_recommendations(self, missing):

        recommendations = []

        for clause in missing:

            recommendations.append(

                f"Consider adding '{clause['clause']}' to strengthen the contract."

            )

        if not recommendations:

            recommendations.append(

                "No major contractual improvements are recommended."

            )

        return recommendations

    # -------------------------------------------------------
    # Main Analysis
    # -------------------------------------------------------

    def analyze(self, text):

        classification = self.classifier.classify(text)

        detected = classification["detected"]

        missing = classification["missing"]

        statistics = classification["statistics"]

        keywords = classification["keywords_found"]

        risk, score, risk_factors = self.calculate_risk(detected)

        health = self.calculate_health(
            missing,
            risk
        )

        verdict = self.generate_verdict(
            health
        )

        summary = self.generate_summary(
            detected,
            missing,
            risk,
            verdict
        )

        warnings = self.generate_warnings(
            detected
        )

        recommendations = self.generate_recommendations(
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

                "risk_score": score,

                "verdict": verdict,

                "summary": summary

            },

            "statistics": statistics,

            "clauses": {

                "detected": detected,

                "missing": missing

            },

            "keywords_found": keywords,

            "risk_factors": risk_factors,

            "warnings": warnings,

            "overall_recommendations": recommendations

        }