import sqlalchemy, DbInitializer
login = input()
password = input()
engine = sqlalchemy.create_engine(f"sqlite:///{login}:{password}@localhost/balance.db")
class Base(sqlalchemy.orm.DeclarativeBase):
    pass
allTables = DbInitializer.DbInitialiser()