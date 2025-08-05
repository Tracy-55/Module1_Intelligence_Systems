from classifier import load_concepts, load_corpus, build_category_matrix, classify
from collections import Counter

# STEP 1: Load list of concept keywords
concepts = load_concepts("concepts.csv")
print(f"\nOriginal concept list:\n{', '.join(concepts)}")

# STEP 2: Load the labeled training dataset (corpus)
corpus = load_corpus("corpus.csv", concepts)

# STEP 3: Display general information about the dataset
print(f"\nReading dataset...")
print(f"{len(corpus.documents)} records loaded in categories:", end=" ")
print(", ".join(sorted(set(doc.category for doc in corpus.documents))))
print(f"First record category: {corpus.documents[0].category}")

# STEP 4: Build a concept matrix (average vector per category)
matrix = build_category_matrix(corpus)

# STEP 5: Display the average concept counts per category
print("\nAverage Concept Counts Per Category:")
header = f"{'Concept':<12}" + "".join(f"Cat {cat:<6}" for cat in sorted(matrix.keys()))
print(header)
for i, concept in enumerate(concepts):
    row = f"{concept:<12}"
    for cat in sorted(matrix.keys()):
        row += f"{matrix[cat][i]:<8.1f}"
    print(row)

# STEP 6: Count and display how many documents exist in each category
print("\nNumber of documents per category:")
cat_counts = Counter(doc.category for doc in corpus.documents)
for cat in sorted(cat_counts.keys()):
    print(f"Category {cat}: {cat_counts[cat]} documents")

# STEP 7: Count how often each concept appears in total across all documents
print("\nTOTAL KEYWORD COUNTS ACROSS ALL RECORDS:")
keyword_totals = {concept: 0 for concept in concepts}
for doc in corpus.documents:
    for i, concept in enumerate(concepts):
        keyword_totals[concept] += doc.vector[i]
for kw, count in sorted(keyword_totals.items(), key=lambda x: -x[1]):
    print(f"{kw}: {count}")

# STEP 8: Load the unseen document and predict its category
with open("unseen.txt", "r", encoding="utf-8") as f:
    unseen_text = f.read()

predicted_category = classify(unseen_text, concepts, matrix)
print(f"\nPredicted category: {predicted_category}")
