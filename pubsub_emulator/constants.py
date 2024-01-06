import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID", "")
LOCAL_URLS_PATH = os.getenv("LOCAL_URLS_PATH", "")
SERVICE_NAME_PATTERN = r"https?://([^/]+)"
LOCAL_BASE_URL = "http://localhost:{port}"
