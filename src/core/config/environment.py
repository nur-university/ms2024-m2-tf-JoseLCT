import os

from dotenv import load_dotenv


class Environment:
    def __init__(self):
        load_dotenv()

        self.database_url = os.getenv("DATABASE_URL")
        self.async_database_url = os.getenv("ASYNC_DATABASE_URL")
