from sqlalchemy import *
from engine import *
import bcrypt

def generate_hash(password: str) -> str:
    """
    Generates a salted hash from the given password string.

    The generated hash is a string that can be stored in a database.
    The salt is randomly generated, and it is used to prevent rainbow table attacks.

    Args:
        password (str): The password string to generate a hash from.

    Returns:
        str: The salted hash of the given password.
    """
    # Generate a salt to prevent rainbow table attacks
    salt = bcrypt.gensalt()

    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Return the hash as a string
    return hashed_password.decode('utf-8')
def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

class Login(Base):
    """
    Represents a login entity for user authentication.

    Attributes:
        id (int): Unique identifier for the login.
        login (str): The username or login identifier.
        password_hash (str): The hashed password for the login.
    """
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True, unique=True)
    login = Column(String(50))
    password_hash = Column(String(50))

    def __init__(self, login, password):
        """
        Initializes a Login object with a login name and password.

        Args:
            login (str): The username or login identifier.
            password (str): The raw password to be hashed.
        """
        self.login = login
        self.password_hash = generate_hash(password)
        self.id = session.query(Login).order_by(Login.id.desc()).first().id + 1
class UsersRecipes(Base):
    __tablename__ = 'users_recipes'
    user_id = Column(Integer)
    recipe_id = Column(Integer, primary_key=True, unique=True)
    table = Column(String(50))
    coef = Column(Float)
    def __init__(self, user_id, recipe_id, table):
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.table = table
class User():
    pass