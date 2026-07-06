from src.clause_classifier.detector import ClauseDetector
from src.clause_classifier.confidence import ConfidenceScorer


class ClauseClassifier:

    def __init__(self):

        self.detector = ClauseDetector()
        self.confidence = ConfidenceScorer()

    def classify(self, text: str):

        detection = self.detector.detect(text)

        detected = detection["detected"]
        keywords = detection["keywords"]

        missing = self.detector.missing(detected)

        detected = self.confidence.calculate(detected)

        return {

            "detected": detected,

            "missing": missing,

            "keywords_found": keywords,

            "statistics": {

                "detected_clauses": len(detected),
                "missing_clauses": len(missing),
                "keywords_found": len(keywords)

            }

        }


if __name__ == "__main__":

    classifier = ClauseClassifier()

    sample = """
    This agreement may be terminated with thirty days notice.
    All confidential information shall remain protected.
    Payment shall be made within thirty days.
    """

    result = classifier.classify(sample)

    from pprint import pprint
    pprint(result)