from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
#from .models import User   Adjust the import as per your project structure
from users.forms import LoginForm  # Import your LoginForm

# Create a Blueprint named 'main'
main = Blueprint('main', __name__)

# Route for the homepage
@main.route('/')
def index():
    return render_template('index.html')

# Route for the farmer login page
@main.route('/farmer-login', methods=['GET', 'POST'])
def farmer_login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check farmer credentials here
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_farmer and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.farmer'))  # Redirect to the farmer's page
        else:
            flash('Invalid credentials, please try again.')  # Show error message
            return redirect(url_for('main.farmer_login'))  # Redirect back to farmer login page
    return render_template('farmer-login.html', form=form)

# Route for the company login page
@main.route('/company-login', methods=['GET', 'POST'])
def company_login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check company credentials here
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_company and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.company'))  # Redirect to the company's page
        else:
            flash('Invalid credentials, please try again.')  # Show error message
            return redirect(url_for('main.company_login'))  # Redirect back to company login page
    return render_template('company-login.html', form=form)

# Route for the agrishop login page
@main.route('/agrishop-login', methods=['GET', 'POST'])
def agrishop_login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check agrishop credentials here
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_agrishop and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.agrishop'))  # Redirect to the agrishop's page
        else:
            flash('Invalid credentials, please try again.')  # Show error message
            return redirect(url_for('main.agrishop_login'))  # Redirect back to agrishop login page
    return render_template('agrishop-login.html', form=form)

# Route for the farmer's page after login
@main.route('/farmer')
@login_required
def farmer():
    if current_user.is_farmer:
        return render_template('farmer.html')
    return redirect(url_for('main.index'))  # Redirect to home if the user is not a farmer

# Route for the company's page after login
@main.route('/company')
@login_required
def company():
    if current_user.is_company:
        return render_template('company.html')
    return redirect(url_for('main.index'))  # Redirect to home if the user is not a company

# Route for the agrishop's page after login
@main.route('/agrishop')
@login_required
def agrishop():
    if current_user.is_agrishop:
        return render_template('agrishop.html')
    return redirect(url_for('main.index'))  # Redirect to home if the user is not an agrishop

# Route for logging out (common logout route)
@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

