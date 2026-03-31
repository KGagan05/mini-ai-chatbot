from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge
with open("data.txt", "r") as f:
    knowledge = f.read().split("\n")

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(knowledge)

def get_response(query):

    query_vec = vectorizer.transform([query])

    similarity = cosine_similarity(query_vec, vectors)
    index = similarity.argmax()

    return knowledge[index]