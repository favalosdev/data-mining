"""Bio Benchmarks Collector."""

from typing import List, Dict, Any

from aire.data.collectors.base_collector import BaseCollector

from aire.config.settings import Settings

class BioBenchmarksCollector(BaseCollector):
    """Collector for Bio benchmarks."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self) -> List[Dict[str, Any]]:
        """Collect bio benchmarks data."""
        return self._mock_data()

    def _mock_data(self) -> List[Dict[str, Any]]:
        """Return mock bio benchmark data."""
        return [
            {
                "name": "Pathogen Detection Accuracy",
                "metric": "Sensitivity",
                "value": 95.0,
                "category": "Bio",
            },
            {
                "name": "Vaccine Efficacy",
                "metric": "Effectiveness Rate",
                "value": 85.5,
                "category": "Bio",
            },
        ]