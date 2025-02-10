from db.db_utils.db_session import create_session
from user import *


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

        This function adjusts the recipe's measures by the given deltas and
        updates the database with the new measures. It also adjusts the
        coefficient for the recipe by multiplying it with 0.9 and ensures
        that the coefficient is never lower than 0.05.

        Args:
            deltas (dict): A dictionary containing the properties and their delta changes.
        """
        with create_session() as session:
            # Create a new measures dictionary by copying the current measures
            newMeasures = self.measures.copy()

            # Iterate through the coeficients of the recipe table
            for (ingridient, tasteAndCoef) in self.table.coeficients.items():
                # Iterate through the taste and coefficient pairs
                for taste, coef in tasteAndCoef.items():
                    # Adjust the measures of the ingridient by the given delta
                    newMeasures[ingridient] += coef * self.measures[ingridient] * self.coef * deltas[taste]

            # Update the measures and apply changes to the database
            self.measures = newMeasures
            session.query(self.table.table).filter(self.table.table.id == self.id).update(newMeasures)

            # Adjust the coefficient for the recipe
            self.coef *= 0.9
            self.coef = max(0.05, self.coef)

            # Update the coefficient in the user's recipe record
            recipeToUser = select(UsersRecipe).where(UsersRecipe.recipe_id == self.id)

            to_change = session.stmt(recipeToUser).one() # FIXME: возможно требует изменения.
            to_change.coef = self.coef

            # Commit the transaction
            session.commit()
