"""
View functions for main application routes.

This module contains the routes and view functions for the main section of the application.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.main.forms import ProjectForm
from app.models import Project


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            deadline=form.deadline.data,
            status='pending'
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('main.index'))
    
    projects = Project.query.all()
    return render_template('main/index.html', form=form, projects=projects)