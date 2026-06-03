from fastapi import FastAPI
from pydantic import BaseModel

from app.pipeline.email_processor import process_email

app = FastAPI()


class EmailRequest(BaseModel):
    content: str


@app.post("/process-email")
def process_email_api(request: EmailRequest):

    return process_email(
        request.content
    )