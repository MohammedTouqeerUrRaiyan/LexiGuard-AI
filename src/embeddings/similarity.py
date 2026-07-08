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
        query,
        documents,
        embeddings=None
    ):

        ranked = self.rank_documents(
            query,
            documents,
            embeddings
        )

        return ranked[0]
    # --------------------------------------------------

    def rank_documents(
        self,
        query: str,
        documents: list,
        embeddings=None
    ):
        """
        Rank documents by cosine similarity.

        If embeddings are already available,
        reuse them instead of encoding again.
        """
        print("Query =", query)
        print("Type  =", type(query))
        query_embedding = self.embedding_model.encode(query)

        if embeddings is None:
            embeddings = self.embedding_model.encode_batch(documents)

        scores = cosine_similarity(
            [query_embedding],
            embeddings
        )[0]

        ranked = []

        for i, score in enumerate(scores):

            ranked.append({

                "document": documents[i],

                "similarity": round(float(score) * 100, 2),

                "index": i

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