"""
Entry point for running the Flask application.

This script imports the create_app function to initialize and run the Flask application.
It also ensures the database is created before the application starts.
"""

from app import create_app
from app.create_db import create_database

# Create the database if it does not exist
create_database()

# Create an application instance using the factory function
app = create_app()

if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
