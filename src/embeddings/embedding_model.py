"""
=========================================================
LexiGuard AI
Embedding Model

Converts contract text into semantic vectors
using Sentence Transformers.

Model:
all-MiniLM-L6-v2

Embedding Size:
384 Dimensions
=========================================================
"""

from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingModel:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Embedding Model Ready.")

    # --------------------------------------------------

    def encode(self, text):

        """
        Convert a single sentence/document
        into an embedding vector.
        """

        embedding = self.model.encode(

            text,

            convert_to_numpy=True,

            normalize_embeddings=True

        )

        return embedding

    # --------------------------------------------------

    def encode_batch(self, documents):

        """
        Encode multiple documents at once.
        """

        embeddings = self.model.encode(

            documents,

            convert_to_numpy=True,

            normalize_embeddings=True

        )

        return embeddings

    # --------------------------------------------------

    def dimension(self):

        """
        Returns embedding dimension.
        """

        return self.model.get_embedding_dimension()

if __name__ == "__main__":

    model = EmbeddingModel()

    text = """
    This agreement shall remain confidential and
    may be terminated with thirty days notice.
    """

    embedding = model.encode(text)

    print()

    print("Embedding Dimension :", model.dimension())

    print()

    print("Vector Shape :", embedding.shape)

    print()

    print("First 15 Values")

    print(embedding[:15])