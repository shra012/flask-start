from flask import Blueprint

cart_controller = Blueprint('cart_controller', __name__,
                            template_folder='templates')
mobile_controller = Blueprint('mobile_controller', __name__,
                              template_folder='templates')

