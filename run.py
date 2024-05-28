"""
Entry point for running the Flask application.

This script imports the create_app function to initialize and run the Flask application.
"""

from app import create_app

# Create an application instance using the factory function
app = create_app()

if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
