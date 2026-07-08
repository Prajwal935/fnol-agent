def generate_summary(fields, classification):
    """
    Generate a short summary of the FNOL claim.
    """

    insured = fields.get("insured_name") or "Unknown Insured"
    incident_date = fields.get("date_of_loss") or "Unknown Date"
    claim_type = classification["claim_type"]

    description = fields.get("description") or "No description provided."

    return (
        f"{claim_type} claim reported by {insured} "
        f"on {incident_date}. {description}"
    )
