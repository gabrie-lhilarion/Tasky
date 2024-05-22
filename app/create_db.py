import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()

def create_database():
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
