"""
Module to initialize the Flask application and its extensions.

This module contains the application factory function and setups for
SQLAlchemy, Flask-Migrate, Flask-Bcrypt, and Flask-Login.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
from flask_moment import Moment
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
moment = Moment()
login_manager.login_view = 'auth.login'  # Redirect to 'auth.login' for login
login_manager.login_message_category = 'info'  # Bootstrap alert category for login messages

def create_app():
    """
    Application factory function to create and configure the Flask app.
    
    Returns:
        app (Flask): Configured Flask application instance.
    """
    app = Flask(__name__)
    
    # Set configuration variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    
    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)

    # Register blueprints
    from app.main import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/')
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    """
    Load user by ID for Flask-Login.

    Args:
        user_id (int): ID of the user.

    Returns:
        User: User instance corresponding to the provided user ID.
    """
    return User.query.get(int(user_id))
