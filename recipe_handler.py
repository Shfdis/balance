from engine import *
from user import *
from DbInitializer import *
class Recipe:
    __slots__ = ["id", "coef", "measures", "recipe_info", "table"]

    def __init__(self, recipe: UsersRecipe):
        """
        Initializes a Recipe object with the given user's recipe.

        Args:
            recipe (UsersRecipe): The user's recipe containing recipe_id, coef, and table.
        """
        self.id = recipe.recipe_id
        self.coef = recipe.coef
        self.table = allTables[recipe.table]
        self.measures = self.table.get_recipe_as_dict(self.id)

    def alter_recipe(self, deltas: dict):
        """
        Alters the recipe's measures based on the provided deltas and updates the database.

        Args:
            deltas (dict): A dictionary containing the properties and their delta changes.
        """
        with sqlalchemy.orm.sessionmaker(engine.engine) as session:
            newMeasures = {}
            for property, delta in deltas.items():
                # Calculate the new measure with the delta and coefficient applied
                newMeasures[property] = self.measures[property] * (1 + delta) * self.coef

            # Update the measures and apply changes to the database
            self.measures = newMeasures
            session.query(self.table.table).filter(self.table.table.id == self.id).update(**newMeasures)

            # Adjust the coefficient for the recipe
            self.coef *= 0.9
            self.coef = max(0.05, self.coef)

            # Update the coefficient in the user's recipe record
            recipeToUser = select(UsersRecipe).where(UsersRecipe.recipe_id == self.id)
            to_change = session.stmt(recipeToUser).one()
            to_change.coef = self.coef

            # Commit the transaction
            session.commit()

            

