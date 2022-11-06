from flask import render_template, url_for,flash, redirect
from .forms import RegistrationForm, LoginForm
from . import app
from .models import User, Post

posts = [
    {
        'title' : "Blogpost 1",
        'author' : "Jhon Doe",
        'date_posted' : "20 April, 2022",
        'content' : "First Blog post" 
    },
    {
        'title' : "Blogpost 2",
        'author' : "Alice Chan",
        'date_posted' : "25 April, 2022",
        'content' : "Second Blog post" 
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def new_route():
    return render_template('about.html',title='About')


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account details for {form.username.data}','success')
        return redirect(url_for('hello'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('hello'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
