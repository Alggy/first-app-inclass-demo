# this is the "app/alpha.py" file

import os
from dotenv import load_dotenv

load_dotenv() # look in the the .env file for env vars

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")
