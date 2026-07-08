import re


def extract_fields(text):

    policy = re.search(r"Policy Number:\s*(.*)", text)
    claim = re.search(r"Claim Number:\s*(.*)", text)
    insured = re.search(r"Insured Name:\s*(.*)", text)
    loss = re.search(r"Date of Loss:\s*(.*)", text)
    vehicle = re.search(r"Vehicle:\s*(.*)", text)
    description = re.search(r"Description of Loss:\s*(.*)", text)

    return {

        "policy_number":
        policy.group(1).strip() if policy else None,

        "claim_number":
        claim.group(1).strip() if claim else None,

        "insured_name":
        insured.group(1).strip() if insured else None,

        "date_of_loss":
        loss.group(1).strip() if loss else None,

        "vehicle":
        vehicle.group(1).strip() if vehicle else None,

        "description":
        description.group(1).strip() if description else None
    }
