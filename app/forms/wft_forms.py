from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    username = StringField("Username : ", validators=[Length(min=5, max=20),DataRequired()])
    password = PasswordField("Password : ", validators=[Length(min=5, max=20),DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField("Login")


class SignUpForm(FlaskForm):
    username = StringField('Username : ', validators=[Length(min=5, max=20), DataRequired()])
    password = PasswordField('New Password', [
        Length(min=5, max=20),
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    email = EmailField('Email : ', validators=[DataRequired(), Email()])
    signup = SubmitField('SignUp')
