import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from db.db_utils.db_session import SqlAlchemyBase


class Recipe(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'recipes'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    default_ingredients = sqlalchemy.Column(sqlalchemy.String)
    change_coefficients = sqlalchemy.Column(sqlalchemy.String)
    tastes = sqlalchemy.Column(sqlalchemy.String)
    