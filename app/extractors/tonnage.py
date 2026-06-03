import re
import dateparser

def extract_vessel_name(text):

    text = text.upper()

    pattern = r"(?:MV|M\/V)\s+([A-Z\s]+?)\s+DWT"

    match = re.search(pattern, text)

    if match:
        return match.group(1).strip()

    return None


def extract_vessel_size(text):

    pattern = r"DWT\s*([\d,]+)"

    match = re.search(
        pattern,
        text.upper()
    )

    if match:
        return match.group(1).replace(",", "")

    return None


def extract_open_port(text):

    pattern = r"OPEN\s+([A-Z\s,]+)"

    match = re.search(
        pattern,
        text.upper()
    )

    if match:

        value = match.group(1)

        value = value.split(",")[0]

        return value.strip()

    return None


def extract_open_date(text):

    pattern = r"O\/A\s+(.*)"

    match = re.search(
        pattern,
        text.upper()
    )

    if match:

        raw_date = match.group(1).strip()

        parsed = dateparser.parse(raw_date)

        if parsed:
            return parsed.date()

    return None


def extract_tonnage(text):

    return {

        "vessel_name":
            extract_vessel_name(text),

        "vessel_size":
            extract_vessel_size(text),

        "open_port":
            extract_open_port(text),

        "open_date":
            str(extract_open_date(text))
    }
    
    import re


def split_tonnage_listings(text):

    pattern = r"(?:MV|M\/V)\s+[A-Z\s]+?DWT[\s\S]*?(?=(?:MV|M\/V)|$)"

    matches = re.findall(
        pattern,
        text.upper()
    )

    return matches

def extract_all_tonnage(text):

    listings = split_tonnage_listings(text)

    vessels = []

    for listing in listings:

        vessel = extract_tonnage(listing)

        vessels.append(vessel)

    return vessels