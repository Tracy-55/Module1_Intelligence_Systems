from models import Document, Corpus
from utils import euclidean_distance, average_vectors
import pandas as pd
import numpy as np

def load_concepts(filepath):
    import csv
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            return [concept.strip().lower() for concept in row]


def load_corpus(filepath, concepts):
    corpus = Corpus()
    df = pd.read_csv(filepath)
    df.columns = ['category', 'title', 'abstract']
    df['category'] = df['category'].astype(str)
    for _, row in df.iterrows():
        doc = Document(row['category'], row['title'], row['abstract'])
        doc.compute_vector(concepts)
        corpus.add_document(doc)
    return corpus

def build_category_matrix(corpus):
    category_vectors = {}
    for cat in corpus.get_categories():
        vectors = [doc.vector for doc in corpus.documents if doc.category == cat]
        category_vectors[cat] = average_vectors(vectors)
    return category_vectors

def classify(text, concepts, category_matrix):
    text = text.lower()
    vec = np.array([text.count(concept) for concept in concepts])
    distances = {cat: euclidean_distance(vec, avg) for cat, avg in category_matrix.items()}
    return min(distances, key=distances.get)

