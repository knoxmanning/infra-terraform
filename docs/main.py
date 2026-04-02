#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import sys
from pathlib import Path

def setup_logging(log_level: str = "INFO") -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Infra-Terraform management tool")
    parser.add_argument(
        "--config",
        type=Path,
        default="config.yaml",
        help="Path to configuration file (default: config.yaml)",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set the logging level (default: INFO)",
    )
    return parser.parse_args()

def main() -> None:
    """Main entry point for the application."""
    args = parse_args()
    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)

    try:
        logger.info("Starting infra-terraform")
        logger.debug(f"Using config file: {args.config}")
        
        if not args.config.exists():
            logger.error(f"Config file not found: {args.config}")
            sys.exit(1)

        # Main application logic would go here
        logger.info("Application completed successfully")

    except Exception as e:
        logger.exception(f"Application failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()