"""AI Evaluations Collector."""

from typing import List, Dict, Any

from aire.data.collectors.base_collector import BaseCollector

from aire.config.settings import Settings

class AIEvaluationsCollector(BaseCollector):
    """Collector for AI evaluations."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self) -> List[Dict[str, Any]]:
        """Collect AI evaluation data."""
        return self._mock_data()

    def _mock_data(self) -> List[Dict[str, Any]]:
        """Return mock AI evaluation data."""
        return [
            {
                "assessment": "Bias Audit",
                "score": 7.5,
                "category": "AI",
                "date": "2023-04-01",
            },
            {
                "assessment": "Safety Review",
                "score": 8.2,
                "category": "AI",
                "date": "2023-05-15",
            },
        ]