import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

# Create logs/ directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("email-agent")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")

# Timed Rotating File Handler
file_handler = TimedRotatingFileHandler(
    filename="logs/email-agent.log",
    when="midnight",
    backupCount=10,
    encoding='utf-8'
)
file_handler.setFormatter(formatter)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Prevent duplicate handlers
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
