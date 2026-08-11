"""Order file upload service foundation.

Supports future CSV/XLSX parsing pipeline for marketplace order reports.
"""

from pathlib import Path

SUPPORTED_EXTENSIONS = {".csv", ".xlsx"}


def validate_file(filename: str) -> bool:
    return Path(filename).suffix.lower() in SUPPORTED_EXTENSIONS


def get_file_type(filename: str) -> str:
    return Path(filename).suffix.lower().replace('.', '')
