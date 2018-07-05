from flask import render_template
from flask import url_for
from flask import redirect
from devthep import app, db, bcrypt
from devthep.form import LoginForm, MyForm, NewBlog
from devthep.models import User, Post
from flask_login import login_user, current_user, logout_user

blogCategory = ['Programming', 'Web Development', 'Computer Science', 'Everyday Life', 'Travelling', 'Careers',
'Software Engineer', 'Mathematics']

examplePost = [
    {
        'Title': 'Biggest Blue Whale in Africa!',
        'Image': 'https://images.unsplash.com/photo-1530728327726-b504480e42ec?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=2e330bf90dfed0f3051eda7c8aa04784&auto=format&fit=crop&w=2089&q=80',
        'Author': 'Thepnathi',
        'Date': "13/08/2017",
        'Content': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    },
    {
        'Title': 'Big Fat Burger!',
        'Image': 'https://images.unsplash.com/photo-1530728327726-b504480e42ec?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=2e330bf90dfed0f3051eda7c8aa04784&auto=format&fit=crop&w=2089&q=80',
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
    # We need to display only the latest blog
    return render_template('home.html', posts = examplePost, title="Hello There")

@app.route("/about")
def about():
    return render_template('about.html', title="About Me")

@app.route("/login", methods=('GET', 'POST'))
def loginFunc():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Login for user
        # User will return none if user data does not exist
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Uses flask login extention to help us login
            # cookie to allow the user to remember if its ticked
            login_user(user)
            return redirect(url_for('home'))
        else:
            return redirect('/login')
    return render_template('login.html', title="Login", form=form)  

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    registerForm = MyForm()
    if registerForm.validate_on_submit():
        print("Welcome " + form.username.data)
        hashPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8', 'strict')
        addNewUser = User(username = form.username.data, email = form.email.data, password = hashPassword)
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
