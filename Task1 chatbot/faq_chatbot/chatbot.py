from faq_data import faqs
from preprocess import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [preprocess(f["question"]) for f in faqs]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_answer(user_input):
    user_input = preprocess(user_input)
    user_vec = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vec, X)
    score = similarity.max()
    index = similarity.argmax()

    # Confidence threshold
    if score < 0.3:
        return "Sorry, I don't understand your question."

    return faqs[index]["answer"]