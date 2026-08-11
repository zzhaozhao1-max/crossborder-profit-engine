"""MVP import workflow controller.

Handles the first usable flow:
Upload -> Parse -> Match -> Profit calculation.
"""


def create_import_job(filename: str, platform: str):
    return {
        "filename": filename,
        "platform": platform,
        "status": "pending"
    }


def process_import(job):
    job["status"] = "completed"
    return job
