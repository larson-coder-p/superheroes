import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
