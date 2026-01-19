"""Base class for data collectors."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseCollector(ABC):
    """Abstract base class for all data collectors."""

    @abstractmethod
    def collect(self) -> List[Dict[str, Any]]:
        """Collect data from the source."""
        pass