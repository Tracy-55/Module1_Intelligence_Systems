# Document Classification System

This project creates a document classification system using Python. It analyzes training documents based on predefined concepts and predicts the category of a new (unseen) document by comparing its concept vector to learned averages. It also relfects my understanding of Python and document classification using concept vectors. The project was built using various programming concepts as part of my coursewirk

# How it Works

1. Load concept terms and training articles.
2. Convert each document into a vector based on concept frequency.
3. Calculates average concept vectors for each category.
4. Reads a new document ('unseen.txt') and vectorizes it.
5. Compares the unseen vector to each category's average using \*\*Euclidean distance.
6. Predicts the category with the smallest distance.

# Programming Concepts Explained

**Procedural Programming**: Functions and control flow (`main.py`, `classifier.py`)

- I used the main.py to maintain that a step by step procedure is followed

**Functional Programming**: Abstractions and vector operations (`utils.py`)

- Functions such as average_vectors() & euclidean_distance() to show abstraction, and NumPy functions are used in a functional style.

**Object-Oriented Programming**: Document and Corpus classes (`models.py`)

- I used Document and Corpus classes to represent data objects.
  **Mathematical Programming**: Vector math, mean, and Euclidean distance
- My understanding is that vectors are calculated and compared using NumPy and Euclidean distance, all of these are key to classification.

# UML Diagrams

'class_diagram.puml': Class structure of the system
'activity_diagram.puml': Visual flow of the algorithm
