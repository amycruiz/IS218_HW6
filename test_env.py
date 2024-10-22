import logging
from dotenv import load_dotenv
import os

load_dotenv()

environment = os.getenv("ENVIRONMENT")
logging.info(f"Running in environment: {environment}")
