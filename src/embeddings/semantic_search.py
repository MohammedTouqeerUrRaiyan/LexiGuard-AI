"""
LexiGuard AI
Semantic Search

Performs semantic retrieval using
EmbeddingModel + VectorStore + SimilarityEngine.
"""

from src.embeddings.vector_store import VectorStore
from src.embeddings.similarity import SimilarityEngine


class SemanticSearch:

    def __init__(self):

        self.store = VectorStore()

        self.similarity = SimilarityEngine()

    # --------------------------------------------------
    # Load Documents
    # --------------------------------------------------

    def load_documents(self, documents):

        """
        documents:

        [
            {
                "text": "...",
                "metadata": {...}
            }
        ]
        """

        self.store.clear()

        self.store.add_documents(documents)

    # --------------------------------------------------
    # Add Single Document
    # --------------------------------------------------

    def add_document(self, text, metadata=None):

        self.store.add_document(
            text,
            metadata
        )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(self, query, top_k=5):

        if self.store.is_empty():
            return []

        docs = self.store.get_documents()

        texts = [
            d["text"]
            for d in docs
        ]

        embeddings = self.store.get_embeddings()

        ranked = self.similarity.rank_documents(
            query,
            texts,
            embeddings
        )

        for item in ranked:

            index = item["index"]

            item["metadata"] = docs[index]["metadata"]

        return ranked[:top_k]
    # --------------------------------------------------
    # Best Match
    # --------------------------------------------------

    def best_match(self, query):

        results = self.search(

            query,

            top_k=1

        )

        if results:

            return results[0]

        return None

    # --------------------------------------------------
    # Total Documents
    # --------------------------------------------------

    def size(self):

        return self.store.size()


# ----------------------------------------------------------
# Testing
# ----------------------------------------------------------

if __name__ == "__main__":

    engine = SemanticSearch()

    engine.load_documents([

        {

            "text":
            "Either party may terminate this agreement with thirty days notice.",

            "metadata":
            {
                "clause": "Termination"
            }

        },

        {

            "text":
            "Employee shall receive salary every month.",

            "metadata":
            {
                "clause": "Payment"
            }

        },

        {

            "text":
            "Confidential information shall not be disclosed.",

            "metadata":
            {
                "clause": "Confidentiality"
            }

        }

    ])

    print("=" * 60)

    print("Semantic Search Test")

    print("=" * 60)

    query = "How can this agreement be ended?"

    print()

    print("Query:")

    print(query)

    print()

    results = engine.search(

        query,

        top_k=3

    )

    print("Top Matches")

    print("-" * 60)

    for result in results:

        print(result)

        print()

    print("=" * 60)