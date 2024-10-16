from flask import Blueprint, render_template, redirect, url_for
from forms import LoginForm, SignUpForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

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
