"""
AIRE (AI Risk Explorer) - Data Mining for AI, Bio, and Loss of Control Risks

This package provides comprehensive tools for collecting, processing, and analyzing
risk-related data from three major categories and three database types.

Categories:
- AI: Artificial Intelligence risks and incidents
- Bio: Biological and biosecurity risks
- Loss of Control: Systemic risks leading to loss of human control

Databases:
- Incidents: Recorded events, accidents, and failures
- Benchmarks: Performance metrics and safety standards
- Evaluations: Risk assessments, audits, and evaluations

Main modules:
- categories: Category-specific data collectors and processors
- databases: Database-specific implementations
- utils: Utility functions for data processing and analysis
- models: Risk assessment and machine learning models
"""

__version__ = "0.1.0"
__author__ = "AIRE Development Team"

from . import categories
from . import databases
from . import utils
from . import models
