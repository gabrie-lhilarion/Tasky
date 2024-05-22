from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    # Create the database if it doesn't exist
    from .create_db import create_database
    create_database()

    return app
