"""
Initialization module for the Tasky application.

This module sets up the Flask application, initializes the SQLAlchemy database, 
and registers the necessary routes and blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()

def create_app():
    """
    Factory function to create and configure the Flask application.

    Returns:
        app (Flask): The configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize database with the Flask app
    db.init_app(app)

    with app.app_context():
        # Import routes
        from .main import routes
        # Create database tables if they don't exist
        db.create_all()

    return app
