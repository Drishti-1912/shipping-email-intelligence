from app.extractors.tonnage import (
    extract_all_tonnage
)

from app.database.crud import (
    save_tonnage
)

with open(
    "sample_emails/tonnage_multi.txt",
    "r",
    encoding="utf-8"
) as f:

    email = f.read()

vessels = extract_all_tonnage(
    email
)

for vessel in vessels:

    save_tonnage(vessel)

print("Saved!")