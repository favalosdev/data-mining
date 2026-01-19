"""Incidents Data Processor."""

from typing import List, Dict, Any

import pandas as pd

from aire.data.processors.base_processor import BaseProcessor

from aire.utils.validators import validate_incident_data

class IncidentsProcessor(BaseProcessor):
    """Processor for incident data."""

    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Validate, clean, and extract features from incident data."""
        validated = validate_incident_data(data)
        if not validated:
            return []

        df = pd.DataFrame(validated)

        # Clean data
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])

        # Feature extraction
        df['description_length'] = df['description'].str.len()
        df['title_length'] = df['title'].str.len()

        # Normalize severity
        df['severity'] = (df['severity'] - df['severity'].min()) / (df['severity'].max() - df['severity'].min())

        return df.to_dict('records')