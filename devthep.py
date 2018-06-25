# Created on 20/06/2018
# Thepnathi Stephenson

from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm
from form import LoginForm
from datetime import datetime

app = Flask(__name__)
# You can generate a secret key by 
# import secrets 
# secrets.token_hex(length_of_key)
# Change and hide secret when deploy
app.config['SECRET_KEY'] ='e9da605dfa4193c24e1a10706c383369'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# SQLlite database 
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# nullable=false - mean it requires the content
class Post(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    date_published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_published}')"

# get current time in dd/mm/yyyy
# date = datetime.datetime.today().strftime('%d-%m-%Y')

blogCategory = ['Programming', 'Web Development', 'Computer Science', 'Everyday Life', 'Travelling', 'Careers',
'Software Engineer', 'Mathematics']

examplePost = [
    {
        'author': 'Thepnathi Stephenson',
        'title': 'Flask Framework for Python',
        'category': 'Programming',
        'date': '101',
        'content': 'Some contents'
    },
    {
        'author': 'Thepnathi Stephenson',
        'title': 'Too many technologies to learn',
        'category': ['Programming', 'Web Development'],
        'date': '01',
        'content': 'Some contents'
    }
]

# Routes Declaration
# Routes will run the function below

# show the latest blog 
# for the home page
def latestPost(blogs):
    for post in blogs:
        if post['author'] == 'Thepnathi Stephenson':
            return post

# Function below will render/load the html template
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = examplePost, title="Hello There")

@app.route("/about")
def about():
    return render_template('about.html', title="About Me")

@app.route("/register", methods=["GET", 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login")
def loginFunc():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

# Python3 devthep.py 
# to run on debug mode
if __name__ == '__main__':
    app.run(debug=True)