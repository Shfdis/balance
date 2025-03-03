import uuid

import flask
from flask import request
from flask import jsonify
from flask import abort
from db.db_utils import __all_models, db_session
import json
import os

from db.db_utils.db_session import create_session
from db.models.Recipe import Recipe

from db import DbInitializer
from db.models.RecipeUser import RecipeUser
from db.models.Token import Token

blueprint = flask.Blueprint(
    "recipes_users_blueprint",
    __name__,
)


@blueprint.route('/usersToken', methods=['GET'])
def get_users_token():
    """
    Функция принимает параметры запроса с полями recipe_id и user_id и формирует уникальный для пользователя токен.
    Returns: str - токен для пользователя
    """
    with create_session() as session:
        token_id = uuid.uuid4()
        recipe_user = session.query(RecipeUser).filter_by(id=request.args["user_id"]).first()
        if recipe_user is None:
            default_recipe_data = session.query(Recipe).filter_by(id=request.args["recipe_id"]).first()
            recipe_user_last = session.query(RecipeUser).order_by(RecipeUser.id.desc()).first()
            recipe_user = RecipeUser(
                id=recipe_user_last.id if recipe_user_last is not None else 1,
                recipe_origin_id=int(request.args["recipe_id"]),
                user_id=request.args["user_id"],
                recipe_json_data=default_recipe_data.default_ingredients,
            )
            session.add(recipe_user)

        token = Token(
            token_id=str(token_id),
            recipe_user_id=recipe_user.id
        )
        session.add(token)
    return jsonify({"token": str(token_id)})


@blueprint.route('/submit/<token>', method=['POST'])
def submitForm(token):
    with create_session() as session:
        token = session.query(Token).filter_by(token_id=token).first()
        if token is None:
            return abort(403)
        recipe_user = session.query(RecipeUser).filter_by(id=token.recipe_user_id).first()
        recipe_user.recipe_origin # - конкретный рецепт пользователя
