# config.py
import os

class Config:
    FLASK_APP = 'run.py'
    FLASK_ENV = 'development'
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:chisom1984@localhost/tasky_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
