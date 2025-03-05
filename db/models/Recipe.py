import datetime
import json

import sqlalchemy
from db.db_utils.db_session import SqlAlchemyBase


class Recipe(SqlAlchemyBase):
    __tablename__ = 'recipes'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    default_ingredients = sqlalchemy.Column(sqlalchemy.String)
    change_coefficients = sqlalchemy.Column(sqlalchemy.String)
    tastes = sqlalchemy.Column(sqlalchemy.String)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'default_ingredients': json.loads(self.default_ingredients),
            'change_coefficients': json.loads(self.change_coefficients),
            'tastes': json.loads(self.tastes)
        }