"""Sync scheduler foundation for marketplace data synchronization."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class SyncTask:
    store_id: str
    platform: str
    status: str = "pending"
    created_at: datetime = datetime.utcnow()


class SyncScheduler:
    def create_task(self, store_id: str, platform: str) -> SyncTask:
        return SyncTask(store_id=store_id, platform=platform)

    def run(self, task: SyncTask):
        task.status = "running"
        return task
