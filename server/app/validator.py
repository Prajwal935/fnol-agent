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

    date_valid = True

    if fields.get("date_of_loss"):

        try:

            datetime.strptime(
                fields["date_of_loss"],
                "%Y-%m-%d"
            )

        except ValueError:

            date_valid = False

    future_date = False

    date_valid = False


    if fields.get("date_of_loss"):
        try:
            datetime.strptime(fields["date_of_loss"], "%Y-%m-%d")
            date_valid = True
        except ValueError:
            date_valid = False

    return {

        "missing_fields": missing_fields,

        "date_valid": date_valid,

        "future_date": future_date,

        "is_valid":
            len(missing_fields) == 0
            and date_valid
            and not future_date

    }
