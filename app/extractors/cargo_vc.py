import re
# extract loading part
def extract_loading_port(text):

    patterns = [
        r"LOAD PORT\s*:\s*(.+)",
        r"LP\s*:\s*(.+)",
        r"POL\s*:\s*(.+)"
    ]

    text = text.upper()

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None

# Extract Discharge Port
def extract_discharge_port(text):

    patterns = [
        r"DISCHARGE PORT\s*:\s*(.+)",
        r"DP\s*:\s*(.+)",
        r"POD\s*:\s*(.+)"
    ]

    text = text.upper()

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None

# Extract cargo name 
def extract_cargo_name(text):

    text = text.upper()

    patterns = [

        r"MTS\s+(.*?)\s+IN\s+BULK",

        r"CARGO\s*:\s*[\d,]+\s*MTS\s+OF\s+(.*?)\s+IN\s+BULK",

        r"MTS\s+(.*?)\n"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        if match:
            return match.group(1).strip()

    return None

# Extract Laycan
import re

def extract_laycan(text):

    text = text.upper()

    patterns = [

        r"LAYCAN\s*:?\s*(.+)",

        r"(\d{1,2}\s*-\s*\d{1,2}\s*[A-Z]+)",

        r"(\d{1,2}\s*[A-Z]+\s*-\s*\d{1,2}\s*[A-Z]+)",

        r"(MID\s+[A-Z]+)",

        r"(END\s+[A-Z]+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None

def extract_account_name(text):

    text = text.upper()

    patterns = [

        r"ACCOUNT\s*:?\s*(.+)",

        r"ACC\s+(.+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None

# Cargo Type
def extract_cargo_type(cargo_name):

    if not cargo_name:
        return None

    cargo_name = cargo_name.upper()

    dry_bulk = [

        "COAL",
        "UREA",
        "IRON SLAG",
        "CLINKER",
        "GRAIN",
        "STEEL"
    ]

    for cargo in dry_bulk:

        if cargo in cargo_name:
            return "DRY BULK"

    return "OTHER"

# combining everything
def extract_vc_cargo(text):

    cargo_name = extract_cargo_name(text)

    return {

        "account_name":
            extract_account_name(text),

        "cargo_name":
            cargo_name,

        "loading_port":
            extract_loading_port(text),

        "discharge_port":
            extract_discharge_port(text),

        "laycan":
            extract_laycan(text),

        "cargo_type":
            extract_cargo_type(cargo_name)
    }
    
    