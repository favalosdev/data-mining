"""Bio Incidents Collector."""

from typing import List, Dict, Any

import requests

from aire.data.collectors.base_collector import BaseCollector

from aire.config.settings import Settings

class BioIncidentsCollector(BaseCollector):
    """Collector for Bio-related incidents."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self) -> List[Dict[str, Any]]:
        """Collect bio incidents from WHO or mock data."""
        try:
            # WHO doesn't have a simple API, so mock
            return self._mock_data()
        except Exception:
            return self._mock_data()

    def _mock_data(self) -> List[Dict[str, Any]]:
        """Return mock bio incident data."""
        return [
            {
                "title": "Pathogen Lab Leak",
                "description": "Accidental release of dangerous pathogen from lab.",
                "date": "2022-12-01",
                "category": "Bio",
                "severity": 0.9,
            },
            {
                "title": "Biosecurity Breach",
                "description": "Unauthorized access to biological materials.",
                "date": "2023-01-20",
                "category": "Bio",
                "severity": 0.6,
            },
        ]