from flask_login import UserMixin
from sqlalchemy_utils import PasswordType
from flask import current_app

from . import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String(80), nullable=False)
    item_name = db.Column(db.String(120), nullable=False)
    item_description = db.Column(db.String(200), nullable=False)
    item_details = db.Column(db.String(240), nullable=False)
    item_image_name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Item {self.id} {self.item_type} {self.item_name} {self.item_description} {self.item_details} {self.item_image_name}>'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(
        PasswordType(
            # The returned dictionary is forwarded to the CryptContext
            onload=lambda **kwargs: dict(
                schemes=current_app.config['PASSWORD_SCHEMES'],
                **kwargs
            ),
        ),
        unique=False,
        nullable=False,
    )
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f'<User {self.id} {self.user_name} {self.email}>'
