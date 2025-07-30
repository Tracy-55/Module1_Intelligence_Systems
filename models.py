class Document:
    def __init__(self, category, title, abstract):
        self.category = category
        self.title = title
        self.abstract = abstract
        self.vector = []

    def compute_vector(self, concepts):
        text = (self.title + " " + self.abstract) .lower ()
        self.vector = [text.count(concept) for concept in concepts]


class Corpus:
    def __init__(self):
        self.documents =[]

    def add_document(self, doc):
        self.documents.append(doc)


    def get_categories(self):
        return list(set(doc.category for doc in self.documents))           