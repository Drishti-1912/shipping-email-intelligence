# Shipping Email Intelligence System

## Overview

This project automates the segregation and extraction of information from shipping emails.

The system classifies incoming emails into:

* TONNAGE
* CARGO_VC (Voyage Charter)
* CARGO_TC (Time Charter)

It then extracts relevant information and stores the results in a structured SQLite database.

---

## Features

* Automatic email classification
* Vessel information extraction
* Voyage charter cargo extraction
* Time charter cargo extraction
* SQLite database storage
* REST API using FastAPI
* Interactive API documentation using Swagger
* Vessel-to-cargo matching engine

---

## Technology Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Streamlit

---

## Project Structure

app/

* classifier/
* extractors/
* pipeline/
* matching/
* database/
* search/

sample_emails/
tests/

dashboard.py
pdf_loader.py
requirements.txt

---

## Installation

Clone the repository:

git clone <repository-url>

Install dependencies:

pip install -r requirements.txt

---

## Run the API

uvicorn app.api:app --reload

Open:

http://127.0.0.1:8000/docs

---

## Example Request

POST /process-email

{
"content": "MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA O/A 2ND JUNE 2026"
}

---

## Example Response

{
"category": "TONNAGE",
"confidence": 100,
"saved": true,
"data": [
{
"vessel_name": "SHENG AN HAI",
"vessel_size": "56564",
"open_port": "XIAMEN",
"open_date": "2026-06-02"
}
]
}

---

## Workflow

Email Input
→ Classification
→ Information Extraction
→ Database Storage
→ JSON Output

---

## Future Enhancements

* Machine Learning based email classification
* Confidence based review queue
* Advanced vessel-cargo matching
* Cloud deployment
* Analytics dashboard

