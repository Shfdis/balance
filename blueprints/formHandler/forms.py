import json

import flask
from flask import abort, jsonify, request

from db.db_utils import __all_models, db_session

from db.db_utils.db_session import create_session
from db.models.RecipeUser import RecipeUser
from db.models.Token import Token

blueprint = flask.Blueprint(
    "form_blueprint",
    __name__,
)

@blueprint.route('/tastes/<user_recipe_id>', methods=['GET'])
def get_all_tastes(user_recipe_id):
    with db_session.create_session() as session:
        tastes = session.query(RecipeUser).where(RecipeUser.id == user_recipe_id).first().recipe_origin.tastes
        return jsonify(json.loads(tastes))

        
@blueprint.route('/submit/<token>', methods=['POST'])
def submit_form(token):
    with create_session() as session:
        token = session.query(Token).filter_by(token=token).first()
        if token is None:
            return abort(403)
        recipe_user = session.query(RecipeUser).filter_by(id=token.recipe_user_id).first()
        recipe_user.recipe_origin # - конкретный рецепт пользователя
        print(request.json, token)

    return {"status": "ok"}

    