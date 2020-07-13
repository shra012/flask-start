from flask import Blueprint
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_login import current_user
from ..model.model import OAuth, db

cart_controller = Blueprint('cart_controller', __name__,
                            template_folder='templates')
mobile_controller = Blueprint('mobile_controller', __name__,
                              template_folder='templates')

google_controller = make_google_blueprint(
    scope=["profile", "email"],
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user),
)

