"""Logging configuration for AIRE."""

import logging

from aire.config.settings import Settings

def setup_logging(settings: Settings) -> None:
    """Set up logging configuration."""
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )