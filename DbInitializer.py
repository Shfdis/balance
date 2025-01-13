import json, RecipeTable
import os
class DbInitialiser:
    """
    Class for initializing the database with recipes.

    Attributes:
        tables (dict): A dictionary of recipe tables, where the key is the table name and the value is the recipe_table object.
    """
    def __init__(self):
        """
        Initializes the db_initialiser.
        """
        self.tables = {}
        self.jsons = {}
        self.load_tables()
    def add_table(self, table: dict) -> None:
        """
        Adds a new recipe table to the database, or changes an existing table

        Args:
            table (dict): The dictionary for the new recipe table. The dictionary should contain the following keys:
                - name (str): The name of the recipe table.
                - tastes (list): A list of strings representing the tastes of the recipe.
                - default_measures (dict): A dictionary containing the default measures for the ingredients.
                - change_coeficients (dict): A dictionary containing the coefficients for changing recipe properties.
        """
        filename = table["name"] + '.json'
        json.dump(table, open('recipes/' + filename, 'w'))
        with open('recipes/' + filename) as json_file:
            data = json.load(json_file)
            self.tables[data["name"]] = RecipeTable.RecipeTable(data)
            self.jsons[data["name"]] = data
    def load_tables(self) -> None:
        """
        Loads all tables from folder recipes.
        """
        for filename in os.listdir('recipes'):
            if filename.endswith(".json"):
                with open('recipes/' + filename) as json_file:
                    data = json.load(json_file)
                    self.tables[data["name"]] = RecipeTable.RecipeTable(data)
                    self.jsons[data["name"]] = data
allTables = DbInitialiser()