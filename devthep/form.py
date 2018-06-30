# Uses flask-wtf to handle form
# https://wtforms.readthedocs.io/en/stable/
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from devthep.models import User

# These gets converted to HTML
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[ DataRequired()])
    email = StringField('Email', validators=[ DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')

    # Check if username or email already exist
    def validate_username(self, username, email):
        user = User.query.filter_by(username = username.data).first()
        email = User.query.filter_by(email = email.data).first()
        if user or email:
            raise ValidationError('That username or email is taken. Please choose a different one')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])