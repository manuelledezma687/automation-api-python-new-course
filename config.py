import os
from dotenv import load_dotenv

env = os.getenv("ENV", "dev")
dotenv_file = f".env.{env}"
load_dotenv(dotenv_file)

class Data:
    BASE_URL = os.getenv("BASE_URL")
    ENVIRONMENT = os.getenv("ENV")
