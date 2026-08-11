from datetime import datetime

class AnalysisTask:
    def __init__(self, task_id, files):
        self.task_id = task_id
        self.files = files
        self.status = "pending"
        self.created_at = datetime.utcnow()
        self.result = None

    def start(self):
        self.status = "processing"

    def complete(self, result):
        self.status = "completed"
        self.result = result

    def fail(self, error):
        self.status = "failed"
        self.result = {"error": error}
