from app.extractors.cargo_tc import extract_tc_cargo
from app.database.crud import save_tc

with open(
    "sample_emails/tc_1.txt",
    "r",
    encoding="utf-8"
) as f:

    email = f.read()

cargo = extract_tc_cargo(email)

save_tc(cargo)

print("TC Saved!")