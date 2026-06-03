import joblib

model = joblib.load(
    "classifier_model.pkl"
)

vectorizer = joblib.load(
    "vectorizer.pkl"
)

def classify_email_ml(text):

    X = vectorizer.transform(
        [text]
    )

    prediction = model.predict(X)

    return prediction[0]