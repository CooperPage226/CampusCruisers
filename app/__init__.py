from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from config import Config


db = SQLAlchemy()
bootstrap = Bootstrap()
login = LoginManager()
login.login_view = 'auth.login'
moment = Moment()


app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = Config.STATIC_FOLDER
app.template_folder = Config.TEMPLATE_FOLDER



from app.Controller.errors import bp_errors as errors
app.register_blueprint(errors)
from app.Controller.auth_routes import bp_auth as auth
app.register_blueprint(auth)
from app.Controller.routes import bp_routes as routes
app.register_blueprint(routes)

from app.Controller import routes,errors
from app.Model import models

def create_app( config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER
    app.template_folder = config_class.TEMPLATE_FOLDER

    db.init_app(app)
    login.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    from app.Controller.errors import bp_errors as errors
    app.register_blueprint(errors)
    from app.Controller.auth_routes import bp_auth as auth
    app.register_blueprint(auth)
    from app.Controller.routes import bp_routes as routes
    app.register_blueprint(routes)
    return app