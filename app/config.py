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
    OAUTHLIB_RELAX_TOKEN_SCOPE = os.getenv(
        "OAUTHLIB_RELAX_TOKEN_SCOPE")  # For OAuth2 in local if any scope is mismatched
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv(
        "OAUTHLIB_INSECURE_TRANSPORT")  # For OAuth2 in local since we use http and not https
    GOOGLE_OAUTH_CLIENT_ID = os.getenv(
        "GOOGLE_OAUTH_CLIENT_ID")  # For Google OAuth2
    GOOGLE_OAUTH_CLIENT_SECRET = os.getenv(
        "GOOGLE_OAUTH_CLIENT_SECRET")  # For Google OAuth2
    FACEBOOK_OAUTH_CLIENT_ID = os.environ.get("FACEBOOK_OAUTH_CLIENT_ID")  # For facebook OAuth2
    FACEBOOK_OAUTH_CLIENT_SECRET = os.environ.get(
        "FACEBOOK_OAUTH_CLIENT_SECRET")  # For facebook OAuth2
    GITHUB_OAUTH_CLIENT_ID = os.environ.get("GITHUB_OAUTH_CLIENT_ID")  # For Github OAuth
    GITHUB_OAUTH_CLIENT_SECRET = os.environ.get(
        "GITHUB_OAUTH_CLIENT_SECRET")  # For Github OAuth