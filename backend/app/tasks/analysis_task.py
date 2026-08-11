"""Analysis task workflow foundation."""


def create_analysis_task(file_id: str):
    return {
        "file_id": file_id,
        "status": "pending",
        "result": None
    }


def complete_task(task, result):
    task["status"] = "completed"
    task["result"] = result
    return task
