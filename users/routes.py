from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from users.forms import LoginForm

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

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# Optional for handling 404 errors
@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
