from datetime import datetime


def validate_fields(fields):

    required_fields = [
        "policy_number",
        "claim_number",
        "insured_name",
        "date_of_loss",
        "vehicle",
        "description"
    ]

    missing_fields = []

    for field in required_fields:
        if not fields.get(field):
            missing_fields.append(field)

    # Validate date format
    date_valid = True

    if fields.get("date_of_loss"):
        try:
            loss_date = datetime.strptime(
                fields["date_of_loss"],
                "%Y-%m-%d"
            )

            # Check if the date is in the future
            future_date = loss_date.date() > datetime.today().date()

        except ValueError:
            date_valid = False
            future_date = False

    else:
        date_valid = False
        future_date = False

    # Overall validation
    is_valid = (
        len(missing_fields) == 0
        and date_valid
        and not future_date
    )

    return {
        "missing_fields": missing_fields,
        "date_valid": date_valid,
        "future_date": future_date,
        "is_valid": is_valid,
        "status": "Valid" if is_valid else "Invalid"
    }
