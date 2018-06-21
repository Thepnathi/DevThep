# Created on 20/06/2018
# Thepnathi Stephenson
import datetime

from flask import Flask, render_template
app = Flask(__name__)

# get current time in dd/mm/yyyy
date = datetime.datetime.today().strftime('%d-%m-%Y')

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

# Function below will render/load the html template
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=examplePost )

@app.route("/about")
def about():
    return render_template('about-me.html', title="About Me")

@app.route("/blog")
def blog():
    return "Blog page"

@app.route("/category")
def category():
    return "Catergories for different blog"

@app.route("/contact")
def conbtact():
    return "How to contact me"

# Python3 devthep.py 
# to run on debug mode
if __name__ == '__main__':
    app.run(debug=True)