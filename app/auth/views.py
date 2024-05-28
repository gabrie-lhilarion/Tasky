"""
View functions for authentication-related actions.

This module contains routes and view functions for handling login,
registration, and logout functionality.
"""

from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app import db, bcrypt
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle login requests and render the login template.

    Returns:
        Response: Redirects to the main page if authenticated, otherwise renders the login template.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))  # Redirect if already logged in

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/login.html', title='Login', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle registration requests and render the registration template.

    Returns:
        Response: Redirects to the login page after successful registration, otherwise renders the registration template.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))  # Redirect if already logged in

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@bp.route('/logout')
def logout():
    """
    Handle logout requests.

    Returns:
        Response: Redirects to the login page after logging out.
    """
    logout_user()
    return redirect(url_for('auth.login'))
