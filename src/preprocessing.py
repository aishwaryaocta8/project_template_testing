"""Data preprocessing utilities."""


def clean_text(text: str) -> str:
    """Clean and normalize text."""
    return text.strip()


def preprocess(data: str) -> str:
    """Preprocess input data."""
    return clean_text(data)

