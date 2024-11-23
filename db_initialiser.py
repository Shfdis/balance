import json, recipe_table

class db_initialiser:
    def __init__(self):
        self.tables = {}
    def add_table(self, file_number): 
        f = open(f'recipes/{file_number}.json', 'r')
        data = json.load(f)
        f.close()
        self.tables[data["name"]] = recipe_table(data)


        