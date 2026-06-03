import re


def extract_account_name(text):

    patterns = [
        r"ACCOUNT\s*:?\s*(.+)",
        r"ACC\s+(.+)"
    ]

    text = text.upper()

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None


def extract_delivery_port(text):

    patterns = [
        r"DELIVERY\s*:?\s*(.+)",
        r"DELY\s*:?\s*(.+)"
    ]

    text = text.upper()

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None


def extract_redelivery_port(text):

    patterns = [
        r"REDELIVERY\s*:?\s*(.+)",
        r"REDEL\s*:?\s*(.+)"
    ]

    text = text.upper()

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None


def extract_duration(text):

    patterns = [

        r"\d+\s*TCT",

        r"ABT\s+\d+\s*DAYS",

        r"\d+\s*-\s*\d+\s*YEARS"
    ]

    text = text.upper()

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(0).strip()

    return None


def extract_laycan(text):

    patterns = [

        r"LC\s+(.+)",

        r"LAYCAN\s*:?\s*(.+)",

        r"(\d{1,2}\s*-\s*\d{1,2}\s*[A-Z]+)"
    ]

    text = text.upper()

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None


def extract_tc_cargo(text):

    return {

        "account_name":
            extract_account_name(text),

        "delivery_port":
            extract_delivery_port(text),

        "redelivery_port":
            extract_redelivery_port(text),

        "duration":
            extract_duration(text),

        "laycan":
            extract_laycan(text)
    }