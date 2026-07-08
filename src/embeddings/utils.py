"""
LexiGuard AI
Embedding Utilities
"""

import numpy as np


# --------------------------------------------------
# Normalize Vector
# --------------------------------------------------

def normalize(vector):

    norm = np.linalg.norm(vector)

    if norm == 0:

        return vector

    return vector / norm


# --------------------------------------------------
# Batch Normalize
# --------------------------------------------------

def normalize_batch(vectors):

    return np.array(

        [

            normalize(v)

            for v in vectors

        ],

        dtype=np.float32

    )


# --------------------------------------------------
# Pretty Print Similarity
# --------------------------------------------------

def similarity_percentage(score):

    return round(score * 100, 2)


# --------------------------------------------------
# Top K Selection
# --------------------------------------------------

def top_k(results, k=5):

    return sorted(

        results,

        key=lambda x: x["similarity"],

        reverse=True

    )[:k]


# --------------------------------------------------
# Remove Duplicate Documents
# --------------------------------------------------

def remove_duplicates(results):

    seen = set()

    unique = []

    for item in results:

        text = item["document"]

        if text not in seen:

            unique.append(item)

            seen.add(text)

    return unique


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)

    print("Embedding Utilities Test")

    print("=" * 60)

    vector = np.array([2, 3, 5], dtype=np.float32)

    print()

    print("Original")

    print(vector)

    print()

    print("Normalized")

    print(normalize(vector))

    print()

    sample = [

        {

            "document": "Clause A",

            "similarity": 81.5

        },

        {

            "document": "Clause B",

            "similarity": 94.8

        },

        {

            "document": "Clause C",

            "similarity": 70.1

        }

    ]

    print("Top 2")

    print(top_k(sample, 2))

    print("=" * 60)