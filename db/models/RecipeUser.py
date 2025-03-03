import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from db.db_utils.db_session import SqlAlchemyBase


class RecipeUser(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users_recipes'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.String)
    change_coef = sqlalchemy.Column(sqlalchemy.Float)
    recipe_json_data = sqlalchemy.Column(sqlalchemy.String)

    recipe_origin_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('recipes.id'))
    recipe_origin = orm.relationship("Recipe")

