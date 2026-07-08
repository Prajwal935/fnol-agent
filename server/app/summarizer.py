def generate_summary(text: str) -> str:
    """
    Generates a short summary of the FNOL document.
    """

    if not text:
        return "No text available for summarization."

    clean_text = " ".join(text.split())

    max_length = 250

    if len(clean_text) <= max_length:
        return clean_text

    summary = clean_text[:max_length]

    last_space = summary.rfind(" ")

    if last_space != -1:
        summary = summary[:last_space]

    return summary + "..."
