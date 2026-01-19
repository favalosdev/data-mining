"""Data validation utilities."""

from typing import Any, Dict, List

import pandas as pd

def validate_incident_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Validate incident data format."""
    required_fields = ["title", "description", "date", "category", "severity"]
    validated = []
    for item in data:
        if all(field in item for field in required_fields):
            validated.append(item)
    return validated

def validate_benchmark_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Validate benchmark data."""
    required_fields = ["name", "metric", "value", "category"]
    validated = []
    for item in data:
        if all(field in item for field in required_fields):
            validated.append(item)
    return validated

def validate_evaluation_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Validate evaluation data."""
    required_fields = ["assessment", "score", "category", "date"]
    validated = []
    for item in data:
        if all(field in item for field in required_fields):
            validated.append(item)
    return validated