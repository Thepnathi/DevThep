from flask import render_template
from flask import url_for
from flask import redirect
from devthep import app
from devthep.form import RegistrationForm
from devthep.form import LoginForm
from devthep.models import User, User

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
