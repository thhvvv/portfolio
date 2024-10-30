from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Create a blueprint for the user routes
user_blueprint = Blueprint('users', __name__)

# Import routes to ensure they are registered with the blueprint
from . import auth, routes, farmer_routes

