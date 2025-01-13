import flask
from flask import request
from flask import jsonify
from flask import make_response
from flask import abort
import json
import os
print(os.getcwd())
import DbInitializer
app = flask.Flask(__name__)
class BusinessHandler:
    def __init__(self):
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.password = data["password"]
    def check(self, request: flask.Request) -> None:
        if request.args.get('password') != self.password:
            abort(401)

businessHandler = BusinessHandler()
@app.route('/recipes', methods=['GET'])
def get_recipes():
    businessHandler.check(request)
    return jsonify(list(DbInitializer.allTables.jsons.values()))

@app.route('/recipes/<id>', methods=['GET'])
def get_recipe(id):
    businessHandler.check(request)
    return jsonify(DbInitializer.allTables.jsons[id])

@app.route('/recipes', methods=['POST'])
def add_recipe():
    businessHandler.check(request)
    print(request.json)
    DbInitializer.allTables.add_table(request.json)
    return jsonify(request.json)
    