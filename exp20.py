import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
# Fit the vectorizer to the documents and transform the documents to TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

# Query
query = "This is the second document."

# Transform the query to a TF-IDF vector
query_vector = vectorizer.transform([query])

# Calculate the cosine similarity between the query vector and the document vectors
cosine_similarities = np.dot(query_vector, tfidf_matrix.T).toarray()[0]

# Get the indices of the documents in descending order of relevance
document_indices = np.argsort(cosine_similarities)[::-1]

# Print the documents and their relevance scores
for index in document_indices:
    print(f"Document: {documents[index]}")
    print(f"Relevance Score: {cosine_similarities[index]}")
    print()
