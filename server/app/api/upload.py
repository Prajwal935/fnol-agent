from fastapi import APIRouter, UploadFile, File, HTTPException, status

from app.parser.fnol import extract_text
from app.extractor import extract_fields
from app.validator import validate_fields
from app.classifier import classify_claim

router = APIRouter()


@router.post("/upload",status_code=status.HTTP_200_OK)
async def upload_document(file: UploadFile = File(...)):
    try:
        text = await extract_text(file)

        if not text:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Could not extract text from uploaded document."
            )

        fields = extract_fields(text)
        validation = validate_fields(fields)
        classification = classify_claim(fields, validation)
        
        return {
            "extractedFields": fields,
            "missingFields": validation["missing_fields"],
            "recommendedRoute": classification["route"],
            "reasoning": classification["reason"]
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
