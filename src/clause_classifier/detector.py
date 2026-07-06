from src.utils.legal_rules import (
    CLAUSE_DATABASE,
    REQUIRED_CLAUSES
)


class ClauseDetector:
    """
    Detects legal clauses using the legal knowledge base.
    """

    def __init__(self):
        self.clauses = CLAUSE_DATABASE

    def detect(self, text: str):

        processed = text.lower()

        detected = []
        keywords_found = []

        for clause_name, info in self.clauses.items():

            matched_keywords = []

            for keyword in info["keywords"]:

                if keyword.lower() in processed:
                    matched_keywords.append(keyword)

            if matched_keywords:

                detected.append({

                    "clause": clause_name,

                    "risk": info["risk"],

                    "importance": info["importance"],

                    "matched_keywords": matched_keywords,

                    "description": info["description"],

                    "recommendation": info["recommendation"]

                })

                keywords_found.extend(matched_keywords)

        return {

            "detected": detected,

            "keywords": list(set(keywords_found))

        }

    def missing(self, detected):

        detected_names = {

            clause["clause"]

            for clause in detected

        }

        missing = []

        for clause in REQUIRED_CLAUSES:

            if clause not in detected_names:

                info = self.clauses[clause]

                missing.append({

                    "clause": clause,

                    "importance": info["importance"],

                    "description": info["description"],

                    "recommendation": info["recommendation"]

                })

        return missing
# ... (your existing imports, classes, and functions)

if __name__ == "__main__":
    print("--- Testing Classifier Script ---")
    
    # 1. Provide some dummy text to test your code
    sample_contract_text = "This Confidentiality Agreement is entered into between..."
    
    print(f"Input text: {sample_contract_text}")
    
    # 2. Call your actual function or class here (replace with your real function name)
    # result = classify_clauses(sample_contract_text)
    # print(f"Classification Result: {result}")
    
    print("--- Script Finished Successfully ---")