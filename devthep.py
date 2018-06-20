# Created on 20/06/2018
# Thepnathi Stephenson
import datetime

from flask import Flask, render_template
app = Flask(__name__)

# get current time in dd/mm/yyyy
date = datetime.datetime.today().strftime('%d-%m-%Y')

blogCategory = ['Programming', 'Web Development', 'Computer Science', 'Everyday Life', 'Travelling', 'Careers',
'Software Engineer', 'Mathematics']

exampleBlog = [
    {
        'author': 'Thepnathi Stephenson',
        'title': 'Introduction to Flask Framework for Python',
        'category': 'Programming',
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
    return render_template('index.html', name="Thepnathi")

@app.route("/about")
def about():
    return render_template('about-me.html')

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