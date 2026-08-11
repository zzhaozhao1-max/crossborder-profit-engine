"""User and store management models for CrossBorder Profit Engine."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Store:
    name: str
    platform: str
    country: str
    currency: str
    active: bool = True


@dataclass
class User:
    user_id: str
    email: str
    stores: List[Store] = field(default_factory=list)
