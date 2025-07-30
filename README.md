# Document Classification System

This project implements a document classification system using Python. It analyzes training documents based on predefined concepts and predicts the category of a new (unseen) document by comparing its concept vector to learned averages.

# How it Works

1. Load concept terms and training articles.
2. Convert each document into a vector based on concept frequency.
3. Calculates average concept vectors for each category.
4. Reads a new document ('unseen.txt') and vectorizes it.
   5.Compares the unseen vector to each category's average using \*\*Euclidean distance.
5. Predicts the category with the smallest distance.

# Programming Concepts Demonstrated

**Procedural Programming**: Functions and control flow (`main.py`, `classifier.py`)
**Functional Programming**: Abstractions and vector operations (`utils.py`)
**Object-Oriented Programming**: Document and Corpus classes (`models.py`)
**Mathematical Programming**: Vector math, mean, and Euclidean distance

# UML Diagrams

'class_diagram.puml': Class structure of the system
'activity_diagram.puml': Visual flow of the algorithm
