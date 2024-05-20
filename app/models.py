"""
Database models for the Tasky application.

This module defines the SQLAlchemy models for the User and Task entities.
"""

from . import db

class User(db.Model):
    """
    Model representing a user in the Tasky application.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The hashed password of the user.
        tasks (list): The list of tasks associated with the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True)

class Task(db.Model):
    """
    Model representing a task in the Tasky application.

    Attributes:
        id (int): The unique identifier for the task.
        title (str): The title of the task.
        description (str): The description of the task.
        due_date (datetime): The due date of the task.
        status (str): The current status of the task.
        user_id (int): The ID of the user who owns the task.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
