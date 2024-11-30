from sqlalchemy import *
import sqlalchemy
import engine
class RecipeTable:
    """
    Represents a table for recipes in the database.

    Attributes:
        table (Table): The SQLAlchemy Table object representing the recipe table.
        tastes (list): List of tastes associated with the recipe.
        default_measures (dict): Default measures for the ingredients.
        coeficients (dict): Coefficients for changing recipe properties.
    """

    def __init__(self, data: dict):
        """
        Initializes the recipe_table with given data.

        Args:
            data (dict): A dictionary containing recipe data, including default measures and tastes.
        """
        columns = []
        self.name = data["name"]
        columns.append(Column("id", Integer, primary_key=True, unique=True))
        for property, value in data["default_measures"].items():
            columns.append(Column(property, Float))
        self.table = Table(self.name, engine.engine, *columns, extend_existing=True)
        self.tastes = data["tastes"]
        self.default_measures = data["default_measures"]
        self.coeficients = data["change_coeficients"]

    def add_recipe(self, measures: dict):
        """
        Adds a new recipe to the recipe table.

        Args:
            measures (dict): A dictionary containing the measures of ingredients for the recipe.
        """
        with sqlalchemy.orm.sessionmaker(engine.engine) as session:
            id = session.query(self.table).order_by(self.table.id.desc()).first().id + 1
            measures["id"] = id
            self.table.insert().values(**measures)

    def get_recipe_as_dict(self, id: int):
        """
        Retrieves a recipe from the table as a dictionary based on the given id.

        Args:
            id (int): The ID of the recipe to retrieve.

        Returns:
            dict: A dictionary representing the recipe, or None if not found.
        """
        with sqlalchemy.orm.sessionmaker(engine.engine) as session:
            recipe = session.query(self.table).filter(self.table.id == id).first()
            return recipe

