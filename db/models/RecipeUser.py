import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from db.db_utils.db_session import SqlAlchemyBase


class UsersToken(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users_recipes'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    # TODO изменить

