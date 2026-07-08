import fitz
from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.filename.endswith(".pdf"):

        pdf_bytes = await file.read()

        document = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in document:
            text += page.get_text()

    elif file.filename.endswith(".txt"):

        text = (await file.read()).decode("utf-8")

    else:

        return {
            "error": "Unsupported file type"
        }

    return {
        "filename": file.filename,
        "text": text
    }
