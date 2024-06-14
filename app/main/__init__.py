"""
Initialization for the main blueprint.

This module creates the Blueprint instance for main routes.
"""

from flask import Blueprint

# Create a Blueprint instance for main routes
main = Blueprint('main', __name__)
from flask_moment import Moment

# Import views to associate with this blueprint
from app.main import views
