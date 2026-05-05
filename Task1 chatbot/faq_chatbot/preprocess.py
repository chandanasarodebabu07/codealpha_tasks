import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [w for w in words if w.isalnum() and w not in stop_words]
    return " ".join(words)