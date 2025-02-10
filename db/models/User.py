from sqlalchemy import orm
import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from db.db_utils.db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    pwd = sqlalchemy.Column(sqlalchemy.String(64), nullable=False, unique=True)
