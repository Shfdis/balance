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
    allTables = DbInitialiser()  # FIXME: подумать над лучшей реализацией динамических таблиц.
    app.register_blueprint(blueprints.recipes.recipes.blueprint)

deploy()

if __name__ == '__main__':
    app.run(debug=True)