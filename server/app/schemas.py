from typing import List, Optional

from pydantic import BaseModel


class ExtractedFields(BaseModel):
    # Policy Information
    policy_number: Optional[str] = None
    policyholder_name: Optional[str] = None
    effective_dates: Optional[str] = None

    # Incident Information
    incident_date: Optional[str] = None
    incident_time: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

    # Involved Parties
    claimant: Optional[str] = None
    third_parties: Optional[str] = None
    contact_details: Optional[str] = None

    # Asset Details
    asset_type: Optional[str] = None
    asset_id: Optional[str] = None
    estimated_damage: Optional[str] = None

    # Other Mandatory Fields
    claim_type: Optional[str] = None
    attachments: Optional[str] = None
    initial_estimate: Optional[str] = None


class ValidationResult(BaseModel):
    missing_fields: List[str]
    status: str


class ClassificationResult(BaseModel):
    claim_type: str
    route: str
    reason: str


class UploadResponse(BaseModel):
    filename: str
    fields: ExtractedFields
    validation: ValidationResult
    classification: ClassificationResult
    summary: str
