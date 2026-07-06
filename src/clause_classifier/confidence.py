from src.utils.legal_rules import CLAUSE_DATABASE


class ConfidenceScorer:
    """
    Computes a confidence score for detected clauses.

    Current strategy:
        confidence = matched_keywords / total_keywords

    Later this can be replaced by an ML classifier probability.
    """

    def __init__(self):
        self.database = CLAUSE_DATABASE

    def calculate(self, detected_clauses):

        results = []

        for clause in detected_clauses:

            clause_name = clause["clause"]

            total_keywords = len(
                self.database[clause_name]["keywords"]
            )

            matched_keywords = len(
                clause["matched_keywords"]
            )

            confidence = round(
                (matched_keywords / total_keywords) * 100
            )

            confidence = max(35, confidence)

            clause["confidence"] = confidence

            results.append(clause)

        return results