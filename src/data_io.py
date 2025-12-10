"""Data I/O utilities."""

import os
from pathlib import Path


def load_data(file_path: str) -> str:
    """Load data from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def save_data(data: str, file_path: str) -> None:
    """Save data to a file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)

