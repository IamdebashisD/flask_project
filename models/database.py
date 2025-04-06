from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

DATABASE_URL: str = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file!")

# Initialize SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True, echo_pool=True)

# Create session
sessionLocal: sessionmaker[Session] = sessionmaker(bind=engine)
session = sessionLocal()

# Define Base for ORM models
Base = declarative_base()