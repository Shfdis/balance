import logging

import flask
from flask import request
from flask import jsonify
from flask import abort
from db.db_utils import __all_models, db_session
import json
import os
from db.db_utils.db_session import create_session
from db.models.Recipe import Recipe
from utils.AuthHandler import AUTH_HANDLER

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

blueprint = flask.Blueprint(
    "recipes_blueprint",
    __name__,
    template_folder="templates",
)



# front gets all nesessary business data
@blueprint.route('/recipes', methods=['GET'])
def get_recipes():
    AUTH_HANDLER.check_login(request)
    with create_session() as session:
        recipes = session.query(Recipe).all()
        return jsonify(list(map(lambda r: r.serialize(), recipes)))


# business API operates with small data and pretty rarely, so it's save to recreate all recipes with every DB query when needed 
@blueprint.route('/recipes', methods=['POST'])
def update_recipes():
    AUTH_HANDLER.check_login(request)
    array_values = request.json
    with create_session() as session:
        with session.begin():
            # delete all previous info
            try:
                session.query(Recipe).delete()
                # recreate recipes
                for recipe in array_values:
                    new_recipe = Recipe()
                    new_recipe.id = recipe["id"]
                    new_recipe.name = recipe["name"]
                    new_recipe.default_ingredients = json.dumps(recipe["default_ingredients"])
                    new_recipe.change_coefficients = json.dumps(recipe["change_coefficients"])
                    new_recipe.tastes = json.dumps(recipe["tastes"])
                    session.add(new_recipe)
            except Exception as e:
                logger.error(e)
                session.rollback()
                return jsonify({"status": "error"})
    logger.debug("successfully update recipes")
    return jsonify({"status": "ok"})
