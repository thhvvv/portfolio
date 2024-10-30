from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here
from .farmer import Farmer
from .company import Company
from .agrishop import AgriShop
from .user import User
from .product import Product
