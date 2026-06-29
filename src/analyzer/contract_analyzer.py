from src.utils.legal_rules import (
    CLAUSE_RULES,
    CLAUSE_EXPLANATIONS,
    CLAUSE_RECOMMENDATIONS,
    CLAUSE_IMPORTANCE,
    CLAUSE_RISK_SCORE
)


class ContractAnalyzer:

    def analyze(self, text: str):

        processed = text.lower()

        clauses_detected = []
        keywords_found = []

        explanations = {}
        recommendations = {}

        total_score = 0

        for clause, keywords in CLAUSE_RULES.items():

            detected = False

            for keyword in keywords:

                if keyword in processed:

                    keywords_found.append(keyword)
                    detected = True

            if detected:

                clauses_detected.append(clause)

                explanations[clause] = CLAUSE_EXPLANATIONS[clause]

                recommendations[clause] = CLAUSE_RECOMMENDATIONS[clause]

                total_score += CLAUSE_RISK_SCORE[clause]

        missing_clauses = []

        for clause in CLAUSE_IMPORTANCE:

            if clause not in clauses_detected:
                missing_clauses.append(clause)

        if total_score >= 15:
            risk = "High"

        elif total_score >= 7:
            risk = "Medium"

        else:
            risk = "Low"

        health = 100

        health -= len(missing_clauses) * 8

        if risk == "Medium":
            health -= 10

        if risk == "High":
            health -= 20

        health = max(0, health)

        if health >= 85:
            summary = "Excellent contract with strong legal protections."

        elif health >= 70:
            summary = "Good contract but improvements are recommended."

        elif health >= 50:
            summary = "Contract contains several legal weaknesses."

        else:
            summary = "High-risk contract. Legal review strongly recommended."

        return {

            "word_count": len(text.split()),

            "character_count": len(text),

            "risk_level": risk,

            "contract_health": health,

            "summary": summary,

            "clauses_detected": clauses_detected,

            "missing_clauses": missing_clauses,

            "keywords_found": list(set(keywords_found)),

            "clause_explanations": explanations,

            "recommendations": recommendations

        }