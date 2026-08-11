"""Base connector interface for marketplace integrations."""

from abc import ABC, abstractmethod


class MarketplaceConnector(ABC):
    @abstractmethod
    def fetch_orders(self):
        raise NotImplementedError

    @abstractmethod
    def fetch_settlements(self):
        raise NotImplementedError
