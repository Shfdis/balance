import sqlalchemy
login = input()
password = input()
engine = sqlalchemy.create_engine(f"mysql+pymysql://{login}:{password}@localhost:3306/recipes")
sess = sqlalchemy.orm.sessionmaker(bind=engine)
class Base(sqlalchemy.orm.DeclarativeBase):
    pass
