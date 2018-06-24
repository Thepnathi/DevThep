# Created on 20/06/2018
# Thepnathi Stephenson
import datetime

from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from form import RegistrationForm
from form import LoginForm
app = Flask(__name__)

# You can generate a secret key by 
# import secrets 
# secrets.token_hex(length_of_key)
# Change and hide secret when deploy
app.config['SECRET_KEY'] ='e9da605dfa4193c24e1a10706c383369'

# get current time in dd/mm/yyyy
date = datetime.datetime.today().strftime('%d-%m-%Y')

now = datetime.datetime.today()

blogCategory = ['Programming', 'Web Development', 'Computer Science', 'Everyday Life', 'Travelling', 'Careers',
'Software Engineer', 'Mathematics']

examplePost = [
    {
        'author': 'Thepnathi Stephenson',
        'title': 'Flask Framework for Python',
        'category': 'Programming',
        'date': date,
        'content': 'Some contents'
    },
    {
        'author': 'Thepnathi Stephenson',
        'title': 'Too many technologies to learn',
        'category': ['Programming', 'Web Development'],
        'date': date,
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

@app.route("/category")
def category():
    return render_template('category.html', title="Blog Category")

@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact")

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