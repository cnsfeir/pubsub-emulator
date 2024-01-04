import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID", "")
