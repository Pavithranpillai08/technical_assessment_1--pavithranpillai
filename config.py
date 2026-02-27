import os
from dotenv import load_dotenv
load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")