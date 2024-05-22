# config.py
import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:chisom1984@localhost/tasky_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
