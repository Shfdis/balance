import json, RecipeTable

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

    def add_table(self, file_name):
        """
        Adds a recipe table to the database from a JSON file.

        Args:
            file_name (str): The name of the JSON file to read from.
        """
        # Open the JSON file in read mode
        with open(f'{file_name}', 'r') as f:
            # Load the JSON data
            data = json.load(f)
        
        # Create a new recipe_table object and add it to the tables dictionary
        self.tables[data["name"]] = RecipeTable(data)


        