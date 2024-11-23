from sqlalchemy import *
import engine
class recipe_table:
    def __init__(self, data: dict):
        columns = []
        columns.append(Column("id", Integer, primary_key=True, unique=True))
        for [property, value] in data["default_measures"].items():
            columns.append(Column(property, Float))
        self.table = Table(self.name, engine.engine, *columns, extend_existing=True) #edit
        self.tastes = data["tastes"]
        self.default_measures = data["default_measures"]
        self.coeficients = data["change_coeficients"]
        self.tastes = data["tastes"]
    def add_recipe(self, measures: dict):
        id = engine.session.query(self.table).order_by(self.table.id.desc()).first().id + 1
        measures["id"] = id
        self.table.insert().values(**measures)
