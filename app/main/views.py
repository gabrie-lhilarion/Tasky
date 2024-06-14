"""
View functions for main application routes.

This module contains the routes and view functions for the main section of the application.
"""

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.main import main
from app.main.forms import ProjectForm, UpdateProjectForm, TaskForm, UpdateTaskForm
from app.models import Project, Task, User, Team


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = ProjectForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                project = Project(
                    title=form.title.data,
                    description=form.description.data,
                    deadline=form.deadline.data,
                    status='pending'
                )

                project.members.append(current_user)
                db.session.add(project)
                db.session.commit()
                flash('Project created successfully!', 'success')
                return redirect(url_for('main.index'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error creating project: {e}', 'danger')
                print(f'Error: {e}')
        else:
            flash('Form validation failed.', 'danger')
            print(f'Form errors: {form.errors}')
  
    assigned_tasks = Task.query.filter_by(assignee_id=current_user.id).all()    # Fetch the tasks assigned to the current user
    projects = Project.query.filter(Project.members.any(id=current_user.id)).all()  # Filter projects by current user
    return render_template('main/index.html', form=form, projects=projects, assigned_tasks=assigned_tasks)

@main.route('/project/<int:project_id>', methods=['GET', 'POST'], endpoint='project_detail')
@login_required
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    form = TaskForm()
    
    if request.method == 'POST':
        try:
            if form.validate_on_submit():
                assignee_id = form.assignee_id.data  # Retrieve assignee ID from the form
                if assignee_id:  # Check if an assignee is selected
                    task = Task(
                        activity=form.activity.data,
                        due_date=form.due_date.data,
                        status = 'pending',
                        assignee_id = assignee_id,  # Associate the selected assignee with the task
                        owner=current_user,
                        project=project
                    )
                    db.session.add(task)
                    db.session.commit()
                    flash('Task added successfully!', 'success')
                    return redirect(url_for('main.project_detail', project_id=project_id))
                else:
                    flash('Please select an assignee for the task.', 'danger')
            else:
                flash('Form validation failed', 'danger')
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')
    
    # Flash form errors
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')

    for task in project.tasks:
        task.assignee_name = User.query.get(task.assignee_id).fullname
    
    return render_template('main/project_detail.html', project=project, form=form)


@main.route('/project/<int:project_id>/update', methods=['GET', 'POST'])
@login_required
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = UpdateProjectForm(obj=project)
    
    if form.validate_on_submit():
        try:
            project.title = form.title.data
            project.description = form.description.data
            project.deadline = form.deadline.data
            db.session.commit()
            flash('Project updated successfully!', 'success')
            return redirect(url_for('main.project_detail', project_id=project_id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating project: {e}', 'danger')
    
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    
    return render_template('main/update_project.html', project=project, form=form)


@main.route('/task/<int:task_id>/update', methods=['GET', 'POST'])
@login_required
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    project = Project.query.get_or_404(task.project_id)
    
    form = UpdateTaskForm(obj=task)
    
    # Populate the assignee field with users
    form.assignee_id.choices = [(user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():
        task.activity = form.activity.data
        task.due_date = form.due_date.data
        task.status = form.status.data
        task.assignee_id = form.assignee_id.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.project_detail', project_id=task.project_id))
    
    return render_template('main/update_task.html', form=form, task=task)


@main.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    project_id = task.project_id
    assignee_id = task.assignee
    
    try:
        db.session.delete(task)
        db.session.commit()
        
        # Check if the assignee has any other tasks in the project
        other_tasks = Task.query.filter_by(project_id=project_id, assignee=assignee_id).count()
        
        if other_tasks == 0:
            # If no other tasks, remove the assignee from the project
            team_member = Team.query.filter_by(user_id=assignee_id, project_id=project_id).first()
            if team_member:
                db.session.delete(team_member)
                db.session.commit()
        
        flash('Task deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting task: {e}', 'danger')
    
    return redirect(url_for('main.project_detail', project_id=project_id))