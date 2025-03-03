import flask
from flask import request
from flask import jsonify
from flask import abort
from db.db_utils import __all_models, db_session
import json
import os

print(os.getcwd())

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
    def check_login(self, func):
        if request.args.get('password') != self.password:
            abort(401)
        return func


businessHandler = BusinessHandler()

# front gets all nesessary business data
@blueprint.route('/recipes', methods=['GET'])
@businessHandler.check_login
def get_recipes():
    businessHandler.check_login(request)
    with create_session() as session:
        return jsonify(session.query(Recipe))


# business API operates with small data and pretty rarely, so it's save to recreate all recipes with every DB query when needed 
@blueprint.route('/recipes', methods=['POST'])
@businessHandler.check_login
def update_recipes():
    print(request.json)
    array_values = json.loads(request.json)["elements"]
    with create_session() as session:
        # delete all previous info
        session.query(Recipe).delete()
        # recreate recipes
        for recipe in array_values:
            new_recipe = Recipe()
            new_recipe.id = recipe["id"]
            new_recipe.name = recipe["name"]
            new_recipe.default_ingredients = jsonify(recipe["default_ingredients"])
            new_recipe.coeficients = jsonify(recipe["coeficients"])
            new_recipe.tastes = jsonify(recipe["tastes"])
            session.add(new_recipe)
        # commit transaction
        session.commit()
    return jsonify(request.json)
