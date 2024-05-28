"""
View functions for main application routes.

This module contains the routes and view functions for the main section of the application.
"""

from flask import render_template
from flask_login import login_required
from app.main import bp

@bp.route('/')
@login_required
def index():
    """
    Render the main index page.

    Returns:
        Response: Renders the index.html template.
    """
    return render_template('main/index.html')
