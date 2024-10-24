from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from werkzeug.security import check_password_hash
from users.forms import LoginForm, SignUpForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    form = LoginForm()
    return render_template('index.html', form=form)

@main.route('/services')
def services():
    return render_template('service.html')

@main.route('/feature')
def feature():
    return render_template('feature.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about us')
def about_us():
    return render_template('about.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic (e.g., check email and password)
        return redirect(url_for('main.dashboard'))
    return render_template('login.html', form=form)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Handle sign up logic
        return redirect(url_for('main.dashboard'))
    return render_template('signup.html', form=form)


# Optional for handling 404 errors
@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
