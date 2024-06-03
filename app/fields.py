# app/fields.py
from wtforms.fields import DateTimeField
from wtforms.widgets import DateTimeInput

class DateTimeLocalInput(DateTimeInput):
    input_type = 'datetime-local'

class DateTimeLocalField(DateTimeField):
    widget = DateTimeLocalInput()
