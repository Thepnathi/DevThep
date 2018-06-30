from flask import render_template
from flask import url_for
from flask import redirect
from devthep import app, db, bcrypt
from devthep.form import RegistrationForm, LoginForm, MyForm
from devthep.models import User, User

blogCategory = ['Programming', 'Web Development', 'Computer Science', 'Everyday Life', 'Travelling', 'Careers',
'Software Engineer', 'Mathematics']

examplePost = [
    {
        'Title': 'Biggest Blue Whale in Africa!',
        'Author': 'Thepnathi',
        'Date': "13/08/2017",
        'Content': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    },
    {
        'Title': 'Big Fat Burger!',
        'Author': 'Thepnathi',
        'Date': "13/08/2017",
        'Content': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }
]

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

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Generate hashed password
        print ("Form validate!")
        hashPassword = bcrypt.generate_password_hash(form.password.data.decode('utf-8'))
        newUser = User(username = form.username.data, email = form.email.data, password = hashPassword)
        db.session.add(newUser)
        db.session.commit()
        return redirect('/home')
    else:
        redirect('/loginFunc')

    return render_template('register.html', title="Register", form=form)

@app.route("/login")
def loginFunc():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/home')
    return render_template('submit.html', form=form)