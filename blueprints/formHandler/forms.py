from db.db_utils import __all_models, db_session
from sqlalchemy import select
blueprint = flask.Blueprint(
    "for,_blueprint",
    __name__,
    template_folder="templates",
)

@blueprint.route('/tastes/<userRecipeId>', methods=['GET'])
def getAllTastes(userRecipeId):
    with db_session.create_session() as session:
        tastes = session.query(UsersRecipe).where(UsersRecipe.id == userRecipeId).first().recipe_origin.tastes
        return tastes

        
@blueprint.route('/submit/<token>', method=['POST'])
def submitForm(token):
    with create_session() as session:
        token = session.query(Token).filter_by(token_id=token).first()
        if token is None:
            return abort(403)
        recipe_user = session.query(RecipeUser).filter_by(id=token.recipe_user_id).first()
        recipe_user.recipe_origin # - конкретный рецепт пользователя

    