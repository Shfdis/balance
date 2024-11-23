from sqlalchemy import *
from engine import *
import bcrypt

def generate_hash(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True, unique=True)
    login = Column(String(50))
    password_hash = Column(String(50))

    def __init__(self, login, password):
        self.login = login
        self.password = generate_hash(password)
        self.id = sess.query(Login).order_by(Login.id.desc()).first().id + 1
class UsersRecipes(Base):
    __tablename__ = 'users_recipes'
    user_id = Column(Integer)
    recipe_id = Column(Integer, primary_key=True)
    table = Column(String(50))
    coef = Column(Float)
    def __init__(self, user_id, recipe_id, table):
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.table = table
class User():
    pass