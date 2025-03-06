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

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

blueprint = flask.Blueprint(
    "recipes_blueprint",
    __name__,
    template_folder="templates",
)

class BusinessHandler:
    def __init__(self):
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.password = data["password"]
    def check_login(self, request):
        if request.args.get('password') != self.password:
            abort(401)


businessHandler = BusinessHandler()

# front gets all nesessary business data
@blueprint.route('/recipes', methods=['GET'])
def get_recipes():
    businessHandler.check_login(request)
    with create_session() as session:
        recipes = session.query(Recipe).all()
        return jsonify(list(map(lambda r: r.serialize(), recipes)))


# business API operates with small data and pretty rarely, so it's save to recreate all recipes with every DB query when needed 
@blueprint.route('/recipes', methods=['POST'])
def update_recipes():
    print(request.json)
    businessHandler.check_login(request)
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
