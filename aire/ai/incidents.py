"""AI Incidents Collector."""

from typing import List, Dict, Any

import requests

from aire.data.collectors.base_collector import BaseCollector

from aire.config.settings import Settings

class AIIncidentsCollector(BaseCollector):
    """Collector for AI-related incidents."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self) -> List[Dict[str, Any]]:
        """Collect AI incidents from AI Incident Database or mock data."""
        try:
            url = self.settings.data_sources["ai_incidents"]
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            incidents = []
            for item in data.get("incidents", []):
                incident = {
                    "title": item.get("title", ""),
                    "description": item.get("description", ""),
                    "date": item.get("date", ""),
                    "category": "AI",
                    "severity": self._calculate_severity(item),
                }
                incidents.append(incident)
            return incidents
        except (requests.RequestException, ValueError):
            # Fallback to mock data
            return self._mock_data()

    def _calculate_severity(self, item: Dict[str, Any]) -> float:
        """Calculate severity score based on incident details."""
        harm = item.get("harm", [])
        return min(len(harm) / 10.0, 1.0)  # Normalize to 0-1

    def _mock_data(self) -> List[Dict[str, Any]]:
        """Return mock AI incident data."""
        return [
            {
                "title": "AI Chatbot Generates Harmful Content",
                "description": "An AI chatbot produced inappropriate responses leading to user distress.",
                "date": "2023-01-15",
                "category": "AI",
                "severity": 0.5,
            },
            {
                "title": "Autonomous Vehicle Accident",
                "description": "Self-driving car caused collision due to software error.",
                "date": "2023-02-20",
                "category": "AI",
                "severity": 0.8,
            },
            {
                "title": "Facial Recognition False Positive",
                "description": "AI system misidentified individual leading to wrongful arrest.",
                "date": "2023-03-10",
                "category": "AI",
                "severity": 0.7,
            },
        ]