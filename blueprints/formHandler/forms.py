import json
import logging

import flask
from flask import abort, jsonify, request

from db.db_utils import __all_models, db_session

from db.db_utils.db_session import create_session
from db.models.RecipeUser import RecipeUser
from db.models.Recipe import Recipe
from db.models.Token import Token
from recipe_handler import RecipeHandler
blueprint = flask.Blueprint(
    "form_blueprint",
    __name__,
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

@blueprint.route('/tastes/<recipe_id>', methods=['GET'])
def get_all_tastes(recipe_id):
    with db_session.create_session() as session:
        tastes = session.query(Recipe).where(Recipe.id == recipe_id).first().tastes
        return jsonify(json.loads(tastes))

        
@blueprint.route('/submit/<token>', methods=['POST'])
def submit_form(token):
    with create_session() as session:
        try:
            token = session.query(Token).filter_by(token=token).first()
            if token is None:
                return abort(403)
            recipe_user = session.query(RecipeUser).filter_by(id=token.recipe_user_id).first()
            session.delete(token)
            handler = RecipeHandler(recipe_user, recipe_user.recipe_origin)
            handler.alter_recipe(request.json, session)
        except Exception as e:
            logger.error(e)
            return {"status": "error", "reason": str(e)}
        session.commit()
    return {"status": "ok"}

    