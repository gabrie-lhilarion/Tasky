"""
Route handlers for the Tasky application.

This module defines the API endpoints for managing tasks, including creating, 
retrieving, updating, and deleting tasks.
"""

from flask import Blueprint, request, jsonify
from .models import db, User, Task

# Define a blueprint for the main routes
bp = Blueprint('main', __name__)

@bp.route('/tasks', methods=['GET', 'POST'])
def tasks():
    """
    Handle the creation and retrieval of tasks.

    GET:
        Retrieve all tasks.

    POST:
        Create a new task with the provided data.

    Returns:
        JSON response with the list of tasks or the created task message.
    """
    if request.method == 'POST':
        data = request.json
        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            due_date=data.get('due_date'),
            status=data.get('status', 'pending'),
            user_id=data['user_id']
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task created successfully"}), 201

    tasks = Task.query.all()
    return jsonify([task.serialize() for task in tasks])

@bp.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task_detail(task_id):
    """
    Handle the retrieval, update, and deletion of a specific task.

    GET:
        Retrieve a task by its ID.

    PUT:
        Update a task by its ID with the provided data.

    DELETE:
        Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve, update, or delete.

    Returns:
        JSON response with the task data, update message, or delete message.
    """
    task = Task.query.get_or_404(task_id)

    if request.method == 'GET':
        return jsonify(task.serialize())

    if request.method == 'PUT':
        data = request.json
        task.title = data['title']
        task.description = data['description']
        task.due_date = data['due_date']
        task.status = data['status']
        db.session.commit()
        return jsonify({"message": "Task updated successfully"})

    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"})
