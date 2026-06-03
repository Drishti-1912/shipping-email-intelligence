from pypdf import PdfReader

from app.pipeline.email_processor import process_email


PDF_PATH = "Shipping Email Segregation (1).pdf"


reader = PdfReader(PDF_PATH)

full_text = ""

for page in reader.pages:

    text = page.extract_text()

    if text:
        full_text += text + "\n"


# Split using document separators
chunks = full_text.split(
    "------------------------------------------------------------------------------------------------------------------------"
)

count = 0
unknown_count = 0

for chunk in chunks:

    chunk = chunk.strip()

    if len(chunk) < 100:
        continue

    try:

        result = process_email(chunk)

        print(
            f"Email {count + 1} -> {result['category']}"
        )

        # DEBUG UNKNOWN EMAILS
        if result["category"] == "UNKNOWN":

            unknown_count += 1

            print("\n" + "=" * 80)
            print(f"UNKNOWN EMAIL #{unknown_count}")
            print("=" * 80)

            print(chunk[:1500])

            print("\n" + "=" * 80 + "\n")

        count += 1

    except Exception as e:

        print("\nERROR PROCESSING EMAIL:")
        print(e)

print("\n")
print("=" * 80)
print(f"Processed: {count}")
print(f"Unknown: {unknown_count}")
print("=" * 80)