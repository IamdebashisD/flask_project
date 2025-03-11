from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:62674123@localhost:3306/flaskApp_customer_db")

engine = create_engine(DATABASE_URL, echo=True)

sessionLocal = sessionmaker(bind=engine)
session = sessionLocal()

Base = declarative_base()