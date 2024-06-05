from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional
from app.fields import DateTimeLocalField 
from app.models import User


class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    deadline = DateTimeField('Deadline', format='%Y-%m-%d %H:%M:%S')
    submit = SubmitField('Create Project')

class TaskForm(FlaskForm):
    activity = TextAreaField('Task', validators=[DataRequired()])
    due_date = DateTimeLocalField('Due Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    assignee = SelectField('Assign to', coerce=int, validators=[DataRequired()])
    status = SelectField('Status', choices=[('pending', 'Pending'), ('completed', 'Completed')], validators=[DataRequired()])
    submit = SubmitField('Add Task')

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.assignee.choices = [(user.id, user.username) for user in User.query.all()]

class UpdateTaskForm(FlaskForm):
    activity = TextAreaField('Task', validators=[DataRequired()])
    due_date = DateTimeField('Due Date', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    assignee = SelectField('Assignee', coerce=int, validators=[DataRequired()])
    status = SelectField('Status', choices=[('pending', 'Pending'), ('completed', 'Completed')], validators=[DataRequired()])
    submit = SubmitField('Update Task')