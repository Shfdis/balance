from flask import Flask
import logging
from flask_restful import Api
from flask_login import LoginManager

import blueprints.recipes.recipes
import db.db_utils.db_session
from db.DbInitializer import DbInitialiser
from config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


@app.route('/')
def index_map():
    return "ok"


def deploy():
    db.db_utils.db_session.global_init("balance.db")
    app.register_blueprint(blueprints.recipes.recipes.blueprint)
    app.register_blueprint(blueprints.formHandler.forms.blueprint)
    app.register_blueprint(blueprints.recipe_user.recipes_users.blueprint)


if __name__ == '__main__':
    deploy()
    app.run(debug=True)