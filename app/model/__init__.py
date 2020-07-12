from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login_page"
login_manager.login_message = "Please Log In to add items to cart"
login_manager.login_message_category = "error"
