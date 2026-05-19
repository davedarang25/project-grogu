# logger.py
import logging

# Configure logging
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(event_message):
    """Log system events with timestamps"""
    logging.info(event_message)