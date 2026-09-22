from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
# Load variables from the .env file
load_dotenv()
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)