from flask import Flask
from flask_wtf.csrf import CSRFProtect

from .model import db, login_manager
from .controllers.cart_controller import cart_controller
from .controllers.mobile_controller import mobile_controller
from .controllers import google_controller, github_controller, facebook_controller
from .cli import add_cli_methods
from .config import Config
from .basic_routes import bootstrap_basic_routes
from .oauth import register_oauth


def bootstrap_wtf_csrf(app):
    csrf = CSRFProtect(app)
    csrf.init_app(app)


def bootstrap_blueprints(app):
    app.register_blueprint(mobile_controller, url_prefix='/mobile')
    app.register_blueprint(cart_controller, url_prefix='/cart')
    app.register_blueprint(google_controller, url_prefix='/login')
    app.register_blueprint(github_controller, url_prefix='/login')
    app.register_blueprint(facebook_controller, url_prefix='/login')


def register_oauth_controllers():
    register_oauth(google_controller)
    register_oauth(facebook_controller)
    register_oauth(github_controller)


def create_app():
    """
    This method is used to create the flask app and bootstrap it with other
    libraries which are used in the project
    :return: Flask
    """
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(Config)
    db.init_app(app)
    bootstrap_wtf_csrf(app)
    login_manager.init_app(app)
    bootstrap_basic_routes(app)
    bootstrap_blueprints(app)
    add_cli_methods(app)
    register_oauth_controllers()
    return app
