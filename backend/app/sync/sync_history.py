"""Synchronization history records."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class SyncRecord:
    store_id: str
    platform: str
    status: str
    synced_at: datetime = datetime.utcnow()
    records_count: int = 0


class SyncHistory:
    def add(self, record: SyncRecord):
        return record
