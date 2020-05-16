"""Application Settings"""

import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")

WRONG_EMAIL = os.getenv("WRONG_EMAIL")
WRONG_PASSWORD = os.getenv("WRONG_PASSWORD")
