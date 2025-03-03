from sqlalchemy import *
import bcrypt


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

class UsersRecipe(Base):
    """
    Represents a relationship between a user and a recipe.

    Attributes:
        user_id (int): The identifier of the user that has the recipe.
        recipe_id (int): The identifier of the recipe.
        table (str): The name of the recipe table.
        coef (float): The coefficient of the recipe.
    """
    __tablename__ = 'users_recipes'
    user_id = Column(Integer)
    recipe_id = Column(Integer, primary_key=True, unique=True)
    table = Column(String(50))
    coef = Column(Float)

    def __init__(self, user_id, recipe_id, table):
        """
        Initializes a UserRecipe object with a user_id, recipe_id and table name.

        Args:
            user_id (int): The identifier of the user that has the recipe.
            recipe_id (int): The identifier of the recipe.
            table (str): The name of the recipe table.
        """
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.table = table

