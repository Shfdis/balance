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
from db.models.RecipeUser import RecipeUser
from db.models.Token import Token
from utils.AuthHandler import AUTH_HANDLER

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
    AUTH_HANDLER.check_login(request)
    with create_session() as session:
        with session.begin():
            token_id = uuid.uuid4()
            recipe_user = session.query(RecipeUser).filter_by(user_id=request.args["user_id"]).first()
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
                token=str(token_id),
                recipe_user_id=recipe_user.id
            )
            session.add(token)
            session.commit()
    return jsonify({"token": str(token_id)})

@blueprint.route('/userRecipe/<recipe_id>/<user_id>', methods=['PUT', 'GET'])
def add_user_recipe(recipe_id, user_id):
    """
    Функция добавляет пользовательский рецепт в базу данных.
    """
    AUTH_HANDLER.check_login(request)
    if request.method == "PUT":
        
        with create_session() as session:
            with session.begin():
                try:
                    newUserRecipe = RecipeUser(
                        user_id=user_id,
                        recipe_json_data=session.query(Recipe).filter_by(id=recipe_id).first().default_ingredients,
                        recipe_origin_id=int(recipe_id)
                    )
                except Exception as e:
                    pass
                session.add(newUserRecipe)
                session.commit()
        return jsonify({"status": "ok"})
    if request.method == "GET":
        with create_session() as session:
            with session.begin():
                try:
                    recipe_user = session.query(RecipeUser).filter_by(user_id=user_id).first()
                    return jsonify({"recipe": json.loads(recipe_user.recipe_json_data)})
                except Exception as e:
                    abort(401)
