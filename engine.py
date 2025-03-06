import sqlalchemy
from sqlalchemy.orm import DeclarativeBase

engine = sqlalchemy.create_engine(f"postgresql+psycopg2://postgresql:postgresql@db:5432/balance")


class Base(DeclarativeBase):
    pass  # DeclarativeBase


metadata = sqlalchemy.MetaData()
