import numpy as np

def euclidean_distance(v1, v2): # Using this to calculate the mathemetical distance
    return np.linalg.norm(v1 - v2)

def average_vectors(vectors):
    if not vectors:
        return[]
    return np.mean(vectors, axis=0)