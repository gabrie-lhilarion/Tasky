"""
Initialization for the auth blueprint.

This module creates the Blueprint instance for authentication-related routes.
"""

from flask import Blueprint

# Create a Blueprint instance for auth routes
bp = Blueprint('auth', __name__)

# Import views to associate with this blueprint
from app.auth import views
