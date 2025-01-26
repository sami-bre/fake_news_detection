import joblib

# Load the logistic regression model
LR_loaded = joblib.load('logistic_regression_model.pkl')

# Load the vectorizer
vectorization_loaded = joblib.load('vectorizer.pkl')

def predict(text: str) -> str:
    cleaned_text = cleaner(text)
    vectorized_text = vectorization_loaded.transform([cleaned_text])
    prediction = LR_loaded.predict(vectorized_text)
    return "Fake" if prediction[0] == 0 else "True"

def cleaner(text: str) -> str:
    import re
    import string
    text = str(text)
    text = text.lower()
    text = re.sub('\\[.*?\\]', '', text)
    text = re.sub("\\\\W", " ", text)
    text = re.sub('https?://\\S+|www\\.\\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\\n', '', text)
    text = re.sub('\\w*\\d\\w*', '', text)
    return text
