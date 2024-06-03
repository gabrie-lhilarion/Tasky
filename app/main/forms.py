from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Optional
from app.fields import DateTimeLocalField 


class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    deadline = DateTimeField('Deadline', format='%Y-%m-%d %H:%M:%S')
    submit = SubmitField('Create Project')

class TaskForm(FlaskForm):
    activity = TextAreaField('Task', validators=[DataRequired()])
    due_date = DateTimeLocalField('Due Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Add Task')