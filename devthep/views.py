from flask import render_template
from flask import url_for
from flask import redirect
from devthep import app, db, bcrypt
from devthep.form import LoginForm, MyForm, NewBlog
from devthep.models import User, Post
from devthep.dummyData import examplePost
from flask_login import login_user, current_user, logout_user
from devthep.quote_api import get_random_quote

# Function below will render/load the html template
@app.route("/")
@app.route("/home")
def home():
    random_quote = get_random_quote()
    print ("SERVER SUCC")
    print (examplePost[0])

    return render_template( 'home.html', 
    postOne = examplePost[0], postTwo = examplePost[1], postThree = examplePost[2],
    title="Dev-Thep Blogging Platform",
    quote = random_quote['quote'], 
    author = random_quote['author'], 
    category = random_quote['cat']
    )

@app.route("/about")
def about():
    return render_template('about.html', title="About Me")

@app.route("/login", methods=('GET', 'POST'))
def loginFunc():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        # Login for user
        # User will return none if user data does not exist
        user = User.query.filter_by(email=loginForm.email.data).first()
        if user and bcrypt.check_password_hash(user.password, loginForm.password.data):
            # Uses flask login extention to help us login
            # cookie to allow the user to remember if its ticked
            login_user(user)
            return redirect(url_for('home'))
        else:
            return redirect('/login')
    return render_template('login.html', title="Login", form=loginForm)  

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    registerForm = MyForm()
    if registerForm.validate_on_submit():
        print("Welcome " + registerForm.username.data)
        hashPassword = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8', 'strict')
        addNewUser = User(username = registerForm.username.data, email = registerForm.email.data, password = hashPassword)
        db.session.add(addNewUser)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('submit.html', title="Register", form = registerForm)

@app.route('/logout', methods=('GET', 'POST'))
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/user')
def user():
    return render_template('user.html', title="User")

# User can publish new post if he/she has been authenticated
@app.route('/publish', methods=('GET', 'POST'))
def publish():
    if (current_user.is_authenticated):
        newBlogForm = NewBlog()
        if newBlogForm.validate_on_submit():
            newPost = Post(title=newBlogForm.title.data, image=newBlogForm.image.data, category=newBlogForm.category.data, content=newBlogForm.content.data)
            db.session.add(newPost)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('publish.html', title = "Create a new post", form = newBlogForm)
    else:
        return redirect(url_for('home'))
