"""
Entry point for running the Tasky application.

This module creates the Flask application instance and runs the development server.
"""

from app import create_app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
