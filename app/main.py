from flask import Flask
import logging
from flask_restful import Api
from flask_cors import CORS
from flask_login import LoginManager

import blueprints.recipes.recipes
import blueprints.recipe_user.recipes_users
import blueprints.formHandler.forms
import db.db_utils.db_session
from config import *

app = Flask(__name__)
CORS(app)
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

deploy()
if __name__ == '__main__':

    app.run(debug=True)