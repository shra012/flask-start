from flask import render_template, abort, redirect, url_for, flash, request, session
from flask_login import login_user,logout_user
from datetime import timedelta

from .forms.wft_forms import LoginForm, SignUpForm
from .model.model import Item, User, db
from .model import login_manager


def bootstrap_basic_routes(app):
    @app.route("/")
    def basic_check():
        return redirect(url_for('home_page'))

    @app.route('/homepage')
    def home_page():
        try:
            items = Item.query.all()
            return render_template("homepage.html", items=items)
        except Exception as e:
            print(e)
            abort(404)

    @app.route('/login', methods=["GET", "POST"])
    def login_page():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None and user.password == form.password.data:
                login_user(user=user, remember=form.remember_me.data, duration=timedelta(hours=24))
                if not form.remember_me.data:
                    session.permanent = True
                return redirect(request.args.get('next') or url_for("home_page"))
            flash('Incorrect Username / Password.', 'error')
        return render_template("login.html", form=form)

    @app.route('/signup', methods=["GET", "POST"])
    def signup_page():
        form = SignUpForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, password=form.password.data, email=form.email.data)
            if user is not None:
                db.session.add(user)
                db.session.commit()
                flash(f'Sign Up Successfully for {user.username} Please Log In', 'success')
                return redirect(request.args.get('next') or url_for("login_page"))
            flash('Please use a different  Username / Email Id.', 'error')
        return render_template("signup.html", form=form)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for('home_page'))
