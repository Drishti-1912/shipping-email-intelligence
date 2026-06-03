from email.mime import text

from app.classifier.classifier import classify_email

from app.extractors.tonnage import extract_all_tonnage

from app.extractors.cargo_vc import extract_vc_cargo

from app.extractors.cargo_tc import extract_tc_cargo

from app.database.crud import (
    save_tonnage,
    save_vc,
    save_tc
)


def process_email(text):

    from app.classifier.ml_classifier import (
        classify_email_ml
    )
    try:

        category, ml_confidence = classify_email_ml(text)

    except:

        category = classify_email(text)

        ml_confidence = 50

    # -------------------
    # TONNAGE
    # -------------------

    if category == "TONNAGE":

        vessels = extract_all_tonnage(text)

        saved_count = 0
        seen = set()

        for vessel in vessels:

            key = (
                vessel["vessel_name"],
                vessel["open_port"],
                vessel["open_date"]
            )

            if key in seen:
                continue

            seen.add(key)

            saved = save_tonnage(vessel)

            if saved:
                saved_count += 1

        confidence = 0

        if vessels:

            v = vessels[0]

            if v.get("vessel_name"):
                confidence += 25

            if v.get("vessel_size"):
                confidence += 25

            if v.get("open_port"):
                confidence += 25

            if v.get("open_date"):
                confidence += 25

        return {
            "category": category,
            "confidence": confidence,
            "saved": saved_count > 0,
            "saved_count": saved_count,
            "data": vessels
        }

    # -------------------
    # VC CARGO
    # -------------------

    elif category == "CARGO_VC":

        cargo = extract_vc_cargo(text)

        saved = save_vc(cargo)

        confidence = 0

        if cargo.get("cargo_name"):
            confidence += 20

        if cargo.get("loading_port"):
            confidence += 20

        if cargo.get("discharge_port"):
            confidence += 20

        if cargo.get("laycan"):
            confidence += 20

        if cargo.get("cargo_type"):
            confidence += 20

        return {
            "category": category,
            "confidence": confidence,
            "saved": saved,
            "data": cargo
        }

    # -------------------
    # TC CARGO
    # -------------------

    elif category == "CARGO_TC":

        cargo = extract_tc_cargo(text)

        saved = save_tc(cargo)

        confidence = 0

        if cargo.get("delivery_port"):
            confidence += 20

        if cargo.get("redelivery_port"):
            confidence += 20

        if cargo.get("duration"):
            confidence += 20

        if cargo.get("laycan"):
            confidence += 20

        if cargo.get("cargo_type"):
            confidence += 20

        return {
            "category": category,
            "confidence": confidence,
            "saved": saved,
            "data": cargo
        }

    # -------------------
    # UNKNOWN
    # -------------------

    return {
        "category": "UNKNOWN",
        "confidence": 0,
        "saved": False,
        "data": None
    }