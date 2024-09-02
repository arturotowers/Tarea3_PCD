from sqlalchemy import Column, Integer, String, JSON
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_email = Column(String, unique=True)
    age = Column(Integer, nullable=True)
    recommendations = Column(JSON, nullable=True)
    ZIP = Column(String, nullable=True)

