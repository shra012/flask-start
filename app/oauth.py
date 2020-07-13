from flask import flash, redirect, url_for
from flask_login import login_user
from flask_dance.consumer import oauth_authorized, oauth_error
from sqlalchemy.orm.exc import NoResultFound

from .model.model import db, User, OAuth


def register_oauth(blueprint):
    # create/login local user on successful OAuth login
    @oauth_authorized.connect_via(blueprint)
    def oauth_logged_in(blueprint, token):
        if not token:
            flash("Failed to log in.", category="error")
            return False
        if blueprint.name == "google":
            resp = blueprint.session.get("/oauth2/v1/userinfo")
        elif blueprint.name == "facebook":
            resp = blueprint.session.get("me?fields=email")
        elif blueprint.name == "github":
            resp = blueprint.session.get("/user")
        else:
            flash("Invalid OAuth Client...", category='error')
            redirect(url_for('login_page'))

        if not resp.ok:
            msg = "Failed to fetch user info."
            flash(msg, category="error")
            return False

        info = resp.json()
        user_id = info["id"]
        username = info["email"].split("@")[0]

        # Find this OAuth token in the database, or create it
        query = OAuth.query.filter_by(provider=blueprint.name, provider_user_id=user_id)
        try:
            oauth = query.one()
        except NoResultFound:
            oauth = OAuth(provider=blueprint.name, provider_user_id=user_id, token=token)

        if oauth.user:
            login_user(oauth.user)
        else:
            # Create a new local user account for this user
            user = User(email=info["email"], username=username)
            # Associate the new local user account with the OAuth token
            oauth.user = user
            # Save and commit our database models
            db.session.add_all([user, oauth])
            db.session.commit()
            # Log in the new local user account
            login_user(user)

        # Disable Flask-Dance's default behavior for saving the OAuth token
        return False

    # notify on OAuth provider error
    @oauth_error.connect_via(blueprint)
    def oauth_handle_error(blueprint, message, response):
        msg = "OAuth error from {name}! " "message={message} response={response}".format(
            name=blueprint.name, message=message, response=response
        )
        flash(msg, category="error")
