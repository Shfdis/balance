import flask
from flask import request
from flask import jsonify
from flask import abort
import json
import os

print(os.getcwd())
from db import DbInitializer

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

    def check(self, request: flask.Request) -> None:
        if request.args.get('password') != self.password:
            abort(401)


businessHandler = BusinessHandler()


@blueprint.route('/recipes', methods=['GET'])
def get_recipes():
    businessHandler.check(request)
    return jsonify(list(DbInitializer.allTables.jsons.values()))


@blueprint.route('/recipes/<id>', methods=['GET'])
def get_recipe(id):
    businessHandler.check(request)
    return jsonify(DbInitializer.allTables.jsons[id])


@blueprint.route('/recipes', methods=['POST'])
def add_recipe():
    businessHandler.check(request)
    print(request.json)
    DbInitializer.allTables.add_table(request.json)
    return jsonify(request.json)
