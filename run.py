# from app.extractors.tonnage import (
#     extract_tonnage,
#     extract_all_tonnage
# )

# from app.extractors.cargo_vc import (
#     extract_vc_cargo
# )

# print("\n========== SINGLE TONNAGE ==========\n")

# with open(
#     "sample_emails/tonnage_1.txt",
#     "r",
#     encoding="utf-8"
# ) as f:

#     tonnage_email = f.read()

# print(
#     extract_tonnage(tonnage_email)
# )

# print("\n========== MULTI TONNAGE ==========\n")

# with open(
#     "sample_emails/tonnage_multi.txt",
#     "r",
#     encoding="utf-8"
# ) as f:

#     multi_tonnage_email = f.read()

# vessels = extract_all_tonnage(
#     multi_tonnage_email
# )

# for vessel in vessels:
#     print(vessel)

# print("\n========== VC CARGO ==========\n")

# with open(
#     "sample_emails/vc_1.txt",
#     "r",
#     encoding="utf-8"
# ) as f:

#     vc_email = f.read()

# print(
#     extract_vc_cargo(vc_email)
# )

# from app.extractors.cargo_vc import extract_vc_cargo

# with open(
#     "sample_emails/vc_real.txt",
#     "r",
#     encoding="utf-8"
# ) as f:

#     vc_email = f.read()

# print(extract_vc_cargo(vc_email))


# from app.extractors.cargo_tc import extract_tc_cargo

# with open(
#     "sample_emails/tc_1.txt",
#     "r",
#     encoding="utf-8"
# ) as f:

#     email = f.read()

# print(extract_tc_cargo(email))

from app.pipeline.processor import process_email

with open(
    "sample_emails/vc_real.txt",
    "r",
    encoding="utf-8"
) as f:

    email = f.read()

print(process_email(email))