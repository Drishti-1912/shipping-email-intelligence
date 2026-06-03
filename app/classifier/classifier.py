def classify_email_rules(text):

    text = text.upper()

    if (
        "DWT" in text
        or "OPEN" in text
        or "MV " in text
    ):
        return "TONNAGE"

    if (
        "LOAD PORT" in text
        or "DISCHARGE PORT" in text
        or "LP:" in text
        or "DP:" in text
        or " LP " in text
        or " DP " in text
        or "IRON SLAG" in text
        or "UREA" in text
    ):  
        return "CARGO_VC"

    if (
        "DELIVERY" in text
        or "REDELIVERY" in text
        or "TCT" in text
    ):
        return "CARGO_TC"

    return "UNKNOWN"

from app.classifier.ml_classifier import classify_email_ml

def classify_email(text):

    try:

        prediction, confidence = classify_email_ml(text)

        # If ML is uncertain, use rules
        if confidence < 70:
            return classify_email_rules(text)

        return prediction

    except Exception:

        return classify_email_rules(text)