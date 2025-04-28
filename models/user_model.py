from sqlalchemy import Column, String, Integer, CHAR
from .database import Base
from sqlalchemy.orm import Mapped
import uuid

def generated_id():
    return str(uuid.uuid4())

class User(Base):
    __tablename__: str = 'users'

    id: Mapped[int] = Column(CHAR(36), primary_key=True, default=generated_id)
    name: Mapped[str] = Column(String(100), nullable=False)
    email: Mapped[str] = Column(String(100), unique=True, nullable=False)

    def __init__(self, name: str, email: str)-> None:
        self.name = name
        self.email = email




