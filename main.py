from classifier import load_concepts, load_corpus, build_category_matrix, classify
concepts = load_concepts("concepts.csv")
corpus = load_corpus("corpus.csv", concepts)
matrix = build_category_matrix(corpus)

with open("unseen.txt", "r", encoding= "utf-8") as f:
    unseen_text = f.read()

    predicted_category = classify(unseen_text, concepts, matrix)
    print(f"Predicted category: {predicted_category}")