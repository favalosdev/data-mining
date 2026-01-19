"""Loss of Control Benchmarks Collector."""

from typing import List, Dict, Any

from aire.data.collectors.base_collector import BaseCollector

from aire.config.settings import Settings

class LOCBenchmarksCollector(BaseCollector):
    """Collector for Loss of Control benchmarks."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self) -> List[Dict[str, Any]]:
        """Collect loss of control benchmarks data."""
        return self._mock_data()

    def _mock_data(self) -> List[Dict[str, Any]]:
        """Return mock loss of control benchmark data."""
        return [
            {
                "name": "Systemic Risk Index",
                "metric": "Risk Score",
                "value": 45.2,
                "category": "Loss of Control",
            },
            {
                "name": "Infrastructure Resilience",
                "metric": "Uptime Percentage",
                "value": 99.5,
                "category": "Loss of Control",
            },
        ]