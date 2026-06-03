import joblib

model = joblib.load(
    "classifier_model.pkl"
)

vectorizer = joblib.load(
    "vectorizer.pkl"
)

def classify_email_ml(text):

    X = vectorizer.transform([text])

    prediction = model.predict(X)[0]

    confidence = round(
        max(model.predict_proba(X)[0]) * 100,
        2
    )

    return prediction, confidence