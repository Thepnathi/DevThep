# Init the app here and bring together component
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] ='e9da605dfa4193c24e1a10706c383369'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogDB.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)

from devthep import views