"""
LexiGuard AI
Vector Store

Stores document embeddings for semantic search.
"""

import numpy as np

from src.embeddings.embedding_model import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.documents = []

        self.embeddings = np.empty(
            (0, 384),
            dtype=np.float32
        )

    # ---------------------------------------------
    # Add One Document
    # ---------------------------------------------

    def add_document(self, text, metadata=None):

        vector = self.embedding_model.encode(text)

        self.documents.append({

            "text": text,

            "metadata": metadata or {}

        })

        self.embeddings = np.vstack(
            (
                self.embeddings,
                vector
            )
        )

    # ---------------------------------------------
    # Add Multiple Documents
    # ---------------------------------------------

    def add_documents(self, documents):

        for doc in documents:

            if isinstance(doc, dict):

                self.add_document(

                    doc["text"],

                    doc.get("metadata", {})

                )

            else:

                self.add_document(doc)

    # ---------------------------------------------
    # Get All Documents
    # ---------------------------------------------

    def get_documents(self):

        return self.documents

    # ---------------------------------------------
    # Get One Document
    # ---------------------------------------------

    def get_document(self, index):

        return self.documents[index]

    # ---------------------------------------------
    # Get All Embeddings
    # ---------------------------------------------

    def get_embeddings(self):

        return self.embeddings

    # ---------------------------------------------
    # Get One Embedding
    # ---------------------------------------------

    def get_embedding(self, index):

        return self.embeddings[index]

    # ---------------------------------------------
    # Store Size
    # ---------------------------------------------

    def size(self):

        return len(self.documents)

    # ---------------------------------------------
    # Empty Check
    # ---------------------------------------------

    def is_empty(self):

        return self.size() == 0

    # ---------------------------------------------
    # Clear Store
    # ---------------------------------------------

    def clear(self):

        self.documents = []

        self.embeddings = np.empty(
            (0, 384),
            dtype=np.float32
        )


# ----------------------------------------------------------
# Test
# ----------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("LexiGuard AI - Vector Store Test")
    print("=" * 60)

    store = VectorStore()

    store.add_document(

        "Either party may terminate this agreement with thirty days notice.",

        {

            "clause": "Termination"

        }

    )

    store.add_document(

        "Employee shall receive salary on the last working day.",

        {

            "clause": "Payment"

        }

    )

    print()

    print("Stored Documents")

    print("-" * 60)

    for i, doc in enumerate(store.get_documents(), start=1):

        print(f"Document {i}")

        print("Clause :", doc["metadata"]["clause"])

        print("Text   :", doc["text"])

        print()

    print("-" * 60)

    print("Documents Stored :", store.size())

    print("Embedding Shape  :", store.get_embeddings().shape)

    print("Embedding Type   :", type(store.get_embeddings()))

    print("=" * 60)