def validate_fields(fields: dict):
    """
    Validate extracted FNOL fields and identify missing mandatory fields.
    """

    mandatory_fields = [
        # Policy Information
        "policy_number",
        "policyholder_name",
        "effective_dates",

        # Incident Information
        "incident_date",
        "incident_time",
        "location",
        "description",

        # Involved Parties
        "claimant",
        "third_parties",
        "contact_details",

        # Asset Details
        "asset_type",
        "asset_id",
        "estimated_damage",

        # Other Mandatory Fields
        "claim_type",
        "attachments",
        "initial_estimate"
    ]

    missing_fields = []

    for field in mandatory_fields:
        value = fields.get(field)

        if value is None or str(value).strip() == "":
            missing_fields.append(field)

    if missing_fields:
        status = "Invalid"
    else:
        status = "Valid"

    return {
        "status": status,
        "missing_fields": missing_fields
    }
