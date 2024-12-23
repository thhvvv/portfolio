from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user
from models.user import User  # Adjust the import based on your structure
from users.forms import LoginForm, SignUpForm
from werkzeug.security import generate_password_hash
from models import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            # Redirect based on the user's role
            if user.role == 'farmer':
                return redirect(url_for('farmer.farmer_dashboard'))
            elif user.role == 'company':
                return redirect(url_for('company.company_dashboard'))
            elif user.role == 'agrishop':
                return redirect(url_for('agrishop.agrishop_dashboard'))
            else:
                return redirect(url_for('main.index'))  # Default redirect
        else:
            flash('Invalid username or password, please try again', 'error')
    return render_template('login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Create and add the new user
        new_user = User(username=form.username.data, password=generate_password_hash(form.password.data))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@auth.route('/request_password', methods=['GET', 'POST'])
def request_password():
    # Your logic for password request
    return render_template('request_password.html')
