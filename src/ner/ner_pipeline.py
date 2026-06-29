import spacy
import en_core_web_md  # Direct import to bypass Windows shortcut/symlink issues
from typing import List, Dict, Any

class LegalNERPipeline:
    def __init__(self):
        """Loads the spaCy processing engine directly from its package package."""
        print("Initializing NLP Engine layout directly...")
        # This bypasses spacy.load string lookups entirely!
        self.nlp = en_core_web_md.load()

    def extract_entities(self, text: str) -> List[Dict[str, Any]]:
        """Analyzes plain text and extracts structured named entities."""
        if not text.strip():
            return []

        doc = self.nlp(text)
        extracted_entities = []

        # Map standard generic labels to contextual legal labels
        label_mapping = {
            "ORG": "PARTY/ORGANIZATION",
            "PERSON": "PARTY/INDIVIDUAL",
            "LAW": "STATUTE/REGULATION",
            "MONEY": "FINANCIAL_VALUE",
            "DATE": "EFFECTIVE_DATE"
        }

        for ent in doc.ents:
            entity_type = label_mapping.get(ent.label_, ent.label_)
            extracted_entities.append({
                "text": ent.text.strip(),
                "label": entity_type,
                "start_char": ent.start_char,
                "end_char": ent.end_char
            })

        return extracted_entities

# Local validation block
if __name__ == "__main__":
    test_contract = (
        "This Agreement is made between LexiGuard-AI Corp and Jane Doe on June 27, 2026. "
        "Pursuant to the Compliance Act of 2022, a maximum fine of $10,000 applies."
    )
    ner = LegalNERPipeline()
    for entity in ner.extract_entities(test_contract):
        print(f"-> [{entity['label']}]: \"{entity['text']}\"")