from fastapi import APIRouter, UploadFile, File

from app.parser.fnol import extract_text
from app.extractor import extract_fields
from app.validator import validate_fields
from app.classifier import classify_claim
from app.summarizer import generate_summary

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    text = await extract_text(file)

    if text is None:
        return {"error": "Unsupported file type"}

    fields = extract_fields(text)

    validation = validate_fields(fields)

    classification = classify_claim(fields)

    summary = generate_summary(fields, classification)

    status = (
        "Ready for Processing"
        if validation["status"] == "Valid"
        else "Needs Review"
    )

    return {
        "filename": file.filename,
        "fields": fields,
        "validation": validation,
        "classification": classification,
        "summary": summary,
        "status": status
    }
