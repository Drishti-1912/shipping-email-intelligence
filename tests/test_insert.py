from app.extractors.cargo_vc import extract_vc_cargo

from app.database.crud import save_vc


with open(
    "sample_emails/vc_real.txt",
    "r",
    encoding="utf-8"
) as f:

    email = f.read()

cargo = extract_vc_cargo(email)

save_vc(cargo)

print("Saved!")