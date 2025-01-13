import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
engine = sqlalchemy.create_engine(f"sqlite:///balance.db")
class Base(DeclarativeBase): 
    pass #DeclarativeBase
metadata = sqlalchemy.MetaData()
