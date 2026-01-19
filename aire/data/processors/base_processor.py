"""Base class for data processors."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseProcessor(ABC):
    """Abstract base class for all data processors."""

    @abstractmethod
    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process the collected data."""
        pass