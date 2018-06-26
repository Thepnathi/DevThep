# Uses flask-wtf to handle form
# https://wtforms.readthedocs.io/en/stable/
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# These gets converted to HTML
class RegistrationForm(FlaskForm):
    username = StringField('Username',
     validators=[
        DataRequired(),
        Length(min=3, max=15)])
    email = StringField('Email',
     validators=[
        DataRequired(),
        Email()])
    password = PasswordField('Password',
     validators=[
        DataRequired(),
        Length(min=6, max=50)])
    confirm_password = PasswordField('Password',
     validators=[
        DataRequired(),
        EqualTo('Password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
     validators=[
        DataRequired(),
        Email()])
    password = PasswordField('Password',
     validators=[
        DataRequired(),
        Length(min=6, max=50)])
    # Secure cookie to remember your detail
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')