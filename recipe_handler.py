from db.db_utils.db_session import create_session
from db.db_utils.__all_models import *
import json
class Recipe:
    def __init__(self, usersRecipe: RecipeUser, recipe: Recipe):
        """
        Initializes a Recipe object with the given user's recipe.

        Args:
            recipe (Recipe): The default recipe.
            usersRecipe (RecipeUser): Recipe of exact user
        """
        self.id = recipe.id
        self.coef = recipe.change_coef
        self.measures = json.loads(usersRecipe.recipe)
        self.changeCoefficients = json.loads(recipe.change_coefficients)
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
            for (ingridient, value) in self.measures.items():
                # Iterate through the taste and coefficient pairs
                for taste, coef in self.change_coefficients[ingridient]:
                    # Adjust the measures of the ingridient by the given delta
                    newMeasures[ingridient] += coef * value * self.coef * deltas[taste]

            # Update the measures and apply changes to the database
            self.measures = newMeasures
            session.query(self.table.table).filter(self.table.table.id == self.id).update(newMeasures)

            # Adjust the coefficient for the recipe
            self.coef *= 0.9
            self.coef = max(0.05, self.coef)

            # Update the coefficient in the user's recipe record
            session.select(RecipeUser.measures).where(UsersRecipe.recipe_id == self.id).update(json.dumps(newMeasures))
            # Commit the transaction
            session.commit()
