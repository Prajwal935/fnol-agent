import re


def get_value(text: str, label_patterns):
    """
    Extract value only from the same line.
    If the value is blank, return None.
    """

    if isinstance(label_patterns, str):
        label_patterns = [label_patterns]

    for label in label_patterns:
        pattern = rf"{label}\s*[:\-]?[ \t]*([^\n\r]*)"

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            value = match.group(1).strip()

            if value == "":
                return None

            headings = [
                "Policy Information",
                "Incident Information",
                "Involved Parties",
                "Asset Details",
                "Other Mandatory Fields",
            ]

            if value in headings:
                return None

            return value

    return None


def extract_fields(text: str):
    fields = {}

    fields["policy_number"] = get_value(
        text,
        [r"Policy\s*Number", r"Policy\s*No\.?"]
    )

    fields["policyholder_name"] = get_value(
        text,
        [r"Policyholder\s*Name", r"Policyholder", r"Insured"]
    )

    fields["effective_dates"] = get_value(
        text,
        r"Effective\s*Dates?"
    )

    fields["incident_date"] = get_value(
        text,
        [r"Incident\s*Date", r"Date\s*of\s*Loss", r"Date"]
    )

    fields["incident_time"] = get_value(
        text,
        [r"Incident\s*Time", r"Time"]
    )

    fields["location"] = get_value(
        text,
        [r"Location", r"Place"]
    )

    fields["description"] = get_value(
        text,
        [r"Description", r"Incident\s*Description"]
    )

    fields["claimant"] = get_value(
        text,
        r"Claimant"
    )

    fields["third_parties"] = get_value(
        text,
        r"Third\s*Parties?"
    )

    fields["contact_details"] = get_value(
        text,
        [r"Contact\s*Details", r"Contact", r"Phone", r"Email"]
    )

    fields["asset_type"] = get_value(
        text,
        [r"Asset\s*Type", r"Vehicle", r"Property"]
    )

    fields["asset_id"] = get_value(
        text,
        [r"Asset\s*ID", r"Vehicle\s*ID", r"VIN"]
    )

    damage = get_value(
        text,
        [r"Estimated\s*Damage", r"Damage"]
    )

    if damage:
        damage = re.sub(r"[₹$,]", "", damage).strip()

    fields["estimated_damage"] = damage

    fields["claim_type"] = get_value(
        text,
        r"Claim\s*Type"
    )

    fields["attachments"] = get_value(
        text,
        r"Attachments?"
    )

    estimate = get_value(
        text,
        r"Initial\s*Estimate"
    )

    if estimate:
        estimate = re.sub(r"[₹$,]", "", estimate).strip()

    fields["initial_estimate"] = estimate

    return fields
