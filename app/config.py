import os
from datetime import timedelta


class Config(object):
    SECRET_KEY = os.getenv(
        'FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To skip the warnings of flask-sqlalchmey
    SQLALCHEMY_ECHO = True  # To print the sql queries in the console.
    EXPLAIN_TEMPLATE_LOADING = False  # To explain how jinja locates its templates on render template
    PASSWORD_SCHEMES = ['pbkdf2_sha512', 'md5_crypt']  # For encrypting the password before saving in the
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)  # To expire the session if session.permanent is true
    # GOOGLE_OAUTH_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
    # GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
