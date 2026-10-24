def validate_email_text(email_text: str) -> str:
    cleaned = (email_text or "").strip()
    if len(cleaned) < 20:
        raise ValueError("Please provide a more complete original email before improving it.")
    return cleaned


def validate_api_key(api_key: str) -> str:
    cleaned = (api_key or "").strip()
    if len(cleaned) < 10:
        raise ValueError("Please enter a valid Google API key.")
    return cleaned


def validate_recipient(recipient: str) -> str:
    return (recipient or "General").strip() or "General"


def validate_tone(tone: str) -> str:
    return (tone or "Professional").strip() or "Professional"


def validate_length(length: str) -> str:
    return (length or "Balanced").strip() or "Balanced"
