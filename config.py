import os
from dotenv import load_dotenv

load_dotenv() 

class Config:
    SECRET_KEY = '15259ef27820e177915cc1cbc29f0059'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///agritech.db'  # SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
