from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from users.forms import LoginForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    form = LoginForm()
    return render_template('index.html', form=form)

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# Optional for handling 404 errors
@main.errorhandler(404)
def page_not_found(e):
    return redirect('index.html')
