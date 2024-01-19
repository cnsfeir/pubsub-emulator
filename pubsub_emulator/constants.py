import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID", "")
SERVICE_MAPPINGS_PATH = os.getenv("SERVICE_MAPPINGS_PATH", "")
SERVICE_NAME_PATTERN = r"https?://([^/]+)"
LOCAL_BASE_URL = "http://localhost:{port}"
HELP_FLAG = "--help"
TIMESTAMP_FORMAT = "YYYYMMDDHHmmss"
CONFIGURATIONS_DIRECTORY = ".configurations"
