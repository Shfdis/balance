import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from db.db_utils.db_session import SqlAlchemyBase


class Token(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users_tokens'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    token = sqlalchemy.Column(sqlalchemy.String)
    recipe_user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users_recipes.id'))
    recipe_user = orm.relationship("RecipeUser")

