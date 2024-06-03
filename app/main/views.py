"""
View functions for main application routes.

This module contains the routes and view functions for the main section of the application.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.main import main
from app.main.forms import ProjectForm, TaskForm
from app.models import Project, Task


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

    projects = Project.query.filter(Project.members.any(id=current_user.id)).all()  # Filter projects by current user
    return render_template('main/index.html', form=form, projects=projects)

@main.route('/project/<int:project_id>', methods=['GET', 'POST'], endpoint='project_detail')
@login_required
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    form = TaskForm()
    
    if request.method == 'POST':
        try:
            if form.validate_on_submit():
                task = Task(
                    activity=form.activity.data,
                    due_date=form.due_date.data if form.due_date.data else None,
                    status='pending',
                    owner=current_user,
                    project=project
                )
                db.session.add(task)
                db.session.commit()
                flash('Task added successfully!', 'success')
                return redirect(url_for('main.project_detail', project_id=project_id))
            else:
                flash('Form validation failed', 'danger')
                
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')
    
    # Flash form errors
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    
    return render_template('main/project_detail.html', project=project, form=form)

