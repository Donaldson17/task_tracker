from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Task', validators=[
        DataRequired(), 
        Length(min=1, max=200)
    ])
    submit = SubmitField('Add Task')