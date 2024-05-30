from flask import render_template, request, redirect, url_for
from . import bp
from ..models import db, Task

@bp.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

@bp.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        # Handle the POST request to create a new task
        title = request.form.get('title')
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('main.tasks'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

