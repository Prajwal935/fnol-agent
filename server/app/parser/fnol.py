import fitz
from fastapi import UploadFile


async def extract_text(file: UploadFile):
    if file.filename.endswith(".pdf"):

        pdf_bytes = await file.read()

        document = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in document:
            text += page.get_text()

        return text

    elif file.filename.endswith(".txt"):

        return (await file.read()).decode("utf-8")

    else:
        return None
