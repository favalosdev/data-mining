"""Loss of Control Evaluations Collector."""

from typing import List, Dict, Any

from aire.data.collectors.base_collector import BaseCollector

from aire.config.settings import Settings

class LOCEvaluationsCollector(BaseCollector):
    """Collector for Loss of Control evaluations."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self) -> List[Dict[str, Any]]:
        """Collect loss of control evaluation data."""
        return self._mock_data()

    def _mock_data(self) -> List[Dict[str, Any]]:
        """Return mock loss of control evaluation data."""
        return [
            {
                "assessment": "Systemic Risk Assessment",
                "score": 6.5,
                "category": "Loss of Control",
                "date": "2023-08-01",
            },
            {
                "assessment": "Control Systems Audit",
                "score": 8.5,
                "category": "Loss of Control",
                "date": "2023-09-15",
            },
        ]