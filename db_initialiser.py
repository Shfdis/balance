import json, recipe_table

class db_initialiser:
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
            file_number (int): The number of the JSON file to read from.
        """
        f = open(f'recipes/{file_name}', 'r')
        data = json.load(f)
        f.close()
        self.tables[data["name"]] = recipe_table(data)


        