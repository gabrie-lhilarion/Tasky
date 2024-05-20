"""
Configuration module for the Tasky application.

This module contains the configuration settings for the Flask application,
including secret keys and database URIs.
"""

import os

class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        SECRET_KEY (str): The secret key for session management and CSRF protection.
        SQLALCHEMY_DATABASE_URI (str): The database URI for SQLAlchemy.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to track modifications of objects.
    """
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasky.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
