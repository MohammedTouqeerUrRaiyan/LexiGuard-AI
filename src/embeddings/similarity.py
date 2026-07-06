"""
=========================================================
LexiGuard AI

Semantic Similarity Engine

Uses cosine similarity on sentence embeddings.

=========================================================
"""

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from src.embeddings.embedding_model import EmbeddingModel


class SimilarityEngine:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

    # --------------------------------------------------

    def similarity_score(
        self,
        text1: str,
        text2: str
    ) -> float:
        """
        Returns cosine similarity percentage.
        """

        embedding1 = self.embedding_model.encode(text1)
        embedding2 = self.embedding_model.encode(text2)

        score = cosine_similarity(
            [embedding1],
            [embedding2]
        )[0][0]

        return round(float(score) * 100, 2)

    # --------------------------------------------------

    def most_similar(
        self,
        query: str,
        documents: list
    ):
        """
        Finds the most similar document.
        """

        query_embedding = self.embedding_model.encode(query)

        document_embeddings = self.embedding_model.encode_batch(
            documents
        )

        similarities = cosine_similarity(
            [query_embedding],
            document_embeddings
        )[0]

        best_index = np.argmax(similarities)

        return {

            "document": documents[best_index],

            "similarity": round(float(similarities[best_index]) * 100, 2),

            "index": int(best_index)

        }

    # --------------------------------------------------

    def rank_documents(
        self,
        query: str,
        documents: list
    ):
        """
        Returns every document ranked by similarity.
        """

        query_embedding = self.embedding_model.encode(query)

        embeddings = self.embedding_model.encode_batch(
            documents
        )

        scores = cosine_similarity(
            [query_embedding],
            embeddings
        )[0]

        ranked = []

        for doc, score in zip(documents, scores):

            ranked.append({

                "document": doc,

                "similarity": round(
                    float(score) * 100,
                    2
                )

            })

        ranked.sort(

            key=lambda x: x["similarity"],

            reverse=True

        )

        return ranked
if __name__ == "__main__":

    engine = SimilarityEngine()

    clause1 = (
        "Either party may terminate this agreement "
        "with thirty days notice."
    )

    clause2 = (
        "The contract may be ended by either party "
        "after providing one month's notice."
    )

    clause3 = (
        "Employee shall receive salary every month."
    )

    print()

    print("Similarity Test")

    print("-" * 50)

    similarity = engine.similarity_score(
        clause1,
        clause2
    )

    print(
        f"Clause1 vs Clause2 : {similarity}%"
    )

    similarity = engine.similarity_score(
        clause1,
        clause3
    )

    print(
        f"Clause1 vs Clause3 : {similarity}%"
    )

    print()

    documents = [

        clause1,

        clause2,

        clause3

    ]

    result = engine.most_similar(

        "Termination of agreement",

        documents

    )

    print()

    print("Most Similar")

    print(result)

    print()

    print("Ranking")

    ranking = engine.rank_documents(

        "Termination Clause",

        documents

    )

    for item in ranking:

        print(item)