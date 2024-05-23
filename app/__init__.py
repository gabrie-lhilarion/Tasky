from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()

migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    # Create the database if it doesn't exist
    from .create_db import create_database
    create_database()

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))