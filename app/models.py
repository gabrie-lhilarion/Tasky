from . import db
from datetime import datetime

class User(db.Model):
    """
    User model representing a user of the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    # Relationship for tasks where the user is the owner
    tasks = db.relationship('Task', backref='owner', lazy=True, foreign_keys='Task.user_id')
    
    # Relationship for tasks where the user is the assignee
    assigned_tasks = db.relationship('Task', backref='assignee', lazy=True, foreign_keys='Task.assignee_id')
    
    projects = db.relationship('Project', secondary='team', backref=db.backref('members', lazy='dynamic'), lazy='dynamic')

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
    
    # Foreign key to the user who created the task (owner)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Foreign key to the user to whom the task is assigned
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

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
