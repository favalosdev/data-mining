"""Configuration settings for AIRE."""

from typing import Dict, Optional

import os

class Settings:
    """Application settings loaded from environment variables."""

    def __init__(self) -> None:
        self.database_url: str = os.getenv("DATABASE_URL", "sqlite:///aire.db")
        self.api_keys: Dict[str, Optional[str]] = {
            "newsapi": os.getenv("NEWSAPI_KEY"),
            "arxiv": None,  # arXiv doesn't require API key
            "wikipedia": None,
        }
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        self.data_sources: Dict[str, str] = {
            "ai_incidents": "https://incidentdatabase.ai/api/v1/incidents",
            "bio_incidents": "https://www.who.int/emergencies/disease-outbreak-news",  # Mock URL
            "loc_incidents": "https://en.wikipedia.org/api/rest_v1/page/summary/Systemic_risk",  # Mock URL
        }