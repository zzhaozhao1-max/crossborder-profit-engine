"""File center service.

Handles uploaded marketplace files and analysis task states.
"""

from datetime import datetime


def create_file_record(filename: str, platform: str = "unknown"):
    return {
        "filename": filename,
        "platform": platform,
        "status": "uploaded",
        "created_at": datetime.utcnow().isoformat()
    }


def update_file_status(record, status: str):
    record["status"] = status
    return record
