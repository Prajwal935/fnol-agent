from typing import Dict


def classify_claim(fields: Dict):
    """
    Classify the FNOL claim,
    decide routing,
    and explain the reason.
    """

    text = ""

    # Combine extracted fields into one searchable string
    for value in fields.values():
        if value:
            text += str(value).lower() + " "

    # ------------------------
    # AUTO CLAIM
    # ------------------------
    auto_keywords = [
        "vehicle",
        "car",
        "truck",
        "bike",
        "motorcycle",
        "road",
        "collision",
        "accident",
        "rear-ended",
        "license",
        "traffic"
    ]

    if any(word in text for word in auto_keywords):
        return {
            "claim_type": "Auto",
            "route_to": "Auto Claims Team",
            "reason": "The document contains vehicle-related information and describes a road accident."
        }

    # ------------------------
    # PROPERTY CLAIM
    # ------------------------
    property_keywords = [
        "house",
        "home",
        "building",
        "property",
        "roof",
        "fire",
        "flood",
        "storm",
        "earthquake",
        "window"
    ]

    if any(word in text for word in property_keywords):
        return {
            "claim_type": "Property",
            "route_to": "Property Claims Team",
            "reason": "The document describes damage to a property or building."
        }

    # ------------------------
    # HEALTH CLAIM
    # ------------------------
    health_keywords = [
        "hospital",
        "doctor",
        "medical",
        "injury",
        "patient",
        "surgery",
        "treatment",
        "health",
        "clinic"
    ]

    if any(word in text for word in health_keywords):
        return {
            "claim_type": "Health",
            "route_to": "Health Claims Team",
            "reason": "The document contains medical treatment or injury information."
        }

    # ------------------------
    # DEFAULT
    # ------------------------
    return {
        "claim_type": "Unknown",
        "route_to": "Manual Review Team",
        "reason": "The claim could not be confidently classified."
    }
