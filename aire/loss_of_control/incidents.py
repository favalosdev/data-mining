"""Loss of Control Incidents Collector."""

from typing import List, Dict, Any

import requests

from aire.data.collectors.base_collector import BaseCollector

from aire.config.settings import Settings

class LOCIncidentsCollector(BaseCollector):
    """Collector for Loss of Control incidents."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self) -> List[Dict[str, Any]]:
        """Collect loss of control incidents."""
        return self._mock_data()

    def _mock_data(self) -> List[Dict[str, Any]]:
        """Return mock loss of control incident data."""
        return [
            {
                "title": "Financial System Crash",
                "description": "Global financial system collapse due to algorithmic trading errors.",
                "date": "2008-09-15",
                "category": "Loss of Control",
                "severity": 1.0,
            },
            {
                "title": "Power Grid Failure",
                "description": "Nationwide blackout caused by cascading system failures.",
                "date": "2021-02-15",
                "category": "Loss of Control",
                "severity": 0.9,
            },
        ]