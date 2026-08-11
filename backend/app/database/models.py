"""ORM model definitions for CrossBorder Profit Engine.

Foundation models:
- User
- Workspace
- Store
- PlatformConnection
- Order
- Settlement
- ProfitRecord
- SyncTask

This module defines the SaaS data relationship structure.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: int
    email: str
    role: str = "owner"


@dataclass
class Workspace:
    id: int
    user_id: int
    name: str


@dataclass
class Store:
    id: int
    workspace_id: int
    name: str
    platform: str
    country: str
    currency: str


@dataclass
class PlatformConnection:
    id: int
    store_id: int
    platform: str
    status: str = "active"


@dataclass
class Order:
    id: int
    store_id: int
    order_id: str
    sku: str
    revenue: float


@dataclass
class Settlement:
    id: int
    order_id: str
    amount: float


@dataclass
class ProfitRecord:
    id: int
    store_id: int
    profit: float
    created_at: datetime


@dataclass
class SyncTask:
    id: int
    store_id: int
    status: str = "pending"
