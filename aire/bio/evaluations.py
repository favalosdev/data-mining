"""Bio Evaluations Collector."""

from typing import List, Dict, Any

from aire.data.collectors.base_collector import BaseCollector

from aire.config.settings import Settings

class BioEvaluationsCollector(BaseCollector):
    """Collector for Bio evaluations."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self) -> List[Dict[str, Any]]:
        """Collect bio evaluation data."""
        return self._mock_data()

    def _mock_data(self) -> List[Dict[str, Any]]:
        """Return mock bio evaluation data."""
        return [
            {
                "assessment": "Biosecurity Audit",
                "score": 8.0,
                "category": "Bio",
                "date": "2023-06-01",
            },
            {
                "assessment": "Risk Assessment",
                "score": 7.8,
                "category": "Bio",
                "date": "2023-07-15",
            },
        ]