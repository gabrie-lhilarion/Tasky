"""
Database models for the Tasky application.

This module defines the SQLAlchemy models for users, tasks, teams, and projects.
"""

from datetime import datetime  # Import datetime module
from . import db

class User(db.Model):
    """
    User model representing a user of the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    tasks = db.relationship('Task', backref='owner', lazy=True)
    projects = db.relationship('Project', secondary='team', backref='members', lazy=True)
    
    # Flask-Login required properties and methods
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Task(db.Model):
    """
    Task model representing a task in the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.Text, nullable=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='pending')
    
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    assignee = db.relationship('User', foreign_keys=[assignee_id], backref='assigned_tasks')
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = db.relationship('User', foreign_keys=[user_id], backref='owned_tasks')
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)
    project = db.relationship('Project', backref='project_tasks')

class Team(db.Model):
    """
    Team model representing the many-to-many relationship between users and projects.
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True, nullable=False)

class Project(db.Model):
    """
    Project model representing a project in the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='pending')
    
    tasks = db.relationship('Task', backref='project', lazy=True)
    members = db.relationship('User', secondary='team', backref='user_projects', lazy=True)
