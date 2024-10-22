from flask import Flask, Blueprint, render_template, redirect, url_for, request
from forms import LoginForm, SignUpForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/services')
def services():
    return render_template('service.html')

@main.route('/feature')
def feature():
    return render_template('feature.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')
def about():
    return render_template('about.html')

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

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Optional for handling 404 errors
@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
