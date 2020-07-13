from flask import Blueprint
from flask_dance.contrib import google, github, facebook
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_login import current_user
from ..model.model import OAuth, db

cart_controller = Blueprint('cart_controller', __name__,
                            template_folder='templates')
mobile_controller = Blueprint('mobile_controller', __name__,
                              template_folder='templates')

google_controller = google.make_google_blueprint(
    scope=["profile", "email"],
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user)
)

github_controller = github.make_github_blueprint(
    scope=["profile", "email"],
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user)
)

facebook_controller = facebook.make_facebook_blueprint(
    scope=['email', 'public_profile'],
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user)
)
