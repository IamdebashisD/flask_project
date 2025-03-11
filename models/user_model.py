from sqlalchemy import Column, String, Integer
from .database import Base
from sqlalchemy.orm import Mapped

class User(Base):
    __tablename__: str = 'users'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(100), nullable=False)
    email: Mapped[str] = Column(String(100), unique=True, nullable=False)




