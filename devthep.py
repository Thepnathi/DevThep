# Created on 20/06/2018
# Thepnathi Stephenson
import datetime

from flask import Flask, render_template
app = Flask(__name__)

date = datetime.datetime.today().strftime('%d-%m-%Y')

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
@app.route("/blog")
def blog():
    return render_template('index.html', name="Thepnathi")

@app.route("/about")
def about():
    return render_template('about-me.html')

# Python3 devthep.py 
# to run on debug mode
if __name__ == '__main__':
    app.run(debug=True)