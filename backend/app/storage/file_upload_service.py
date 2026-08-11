"""Production file upload service foundation."""

ALLOWED_EXTENSIONS = ["xlsx", "csv"]


def validate_file(filename: str):
    extension = filename.split(".")[-1].lower()
    return extension in ALLOWED_EXTENSIONS


def create_upload_task(filename: str):
    return {
        "filename": filename,
        "status": "pending"
    }
