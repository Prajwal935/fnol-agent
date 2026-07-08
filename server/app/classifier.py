def classify_claim(fields: dict, validation: dict):
    """
    Classify and route the FNOL claim according to the assessment rules.
    """

    claim_type = (fields.get("claim_type") or "Unknown").strip()

    description = (fields.get("description") or "").lower()

    estimated_damage = fields.get("estimated_damage")

    if validation["missing_fields"]:
        return {
            "claim_type": claim_type,
            "route": "Manual Review",
            "confidence": 0.95,
            "reason": "Mandatory fields are missing, therefore the claim requires manual review."
        }

    fraud_keywords = ["fraud", "staged", "inconsistent"]

    if any(word in description for word in fraud_keywords):
        return {
            "claim_type": claim_type,
            "route": "Investigation Flag",
            "confidence": 0.98,
            "reason": "Suspicious keywords found in the incident description."
        }

    if claim_type.lower() == "injury":
        return {
            "claim_type": "Injury",
            "route": "Specialist Queue",
            "confidence": 0.97,
            "reason": "The claim type is Injury and requires specialist handling."
        }

    if estimated_damage:

        try:

            damage = int(
                str(estimated_damage)
                .replace(",", "")
                .replace("₹", "")
                .strip()
            )

            if damage < 25000:
                return {
                    "claim_type": claim_type,
                    "route": "Fast-track",
                    "confidence": 0.96,
                    "reason": "Estimated damage is below ₹25,000."
                }

        except ValueError:
            pass

    return {
        "claim_type": claim_type,
        "route": "Standard Claims Processing",
        "reason": "Claim meets the standard processing criteria."
    }
