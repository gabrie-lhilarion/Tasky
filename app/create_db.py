"""
Script to create the database if it does not exist.

This module contains a function to connect to the MySQL server and create the
database defined in the environment variables if it does not already exist.
"""

import MySQLdb
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_database():
    """
    Create the database if it does not exist.

    Connects to the MySQL server using credentials from environment variables
    and creates the database specified by the 'DB_NAME' environment variable.
    """
    # Database connection details
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'yourusername')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'yourpassword')
    DB_NAME = os.getenv('DB_NAME', 'tasky_db')

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD)

        cursor = db.cursor()

        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
