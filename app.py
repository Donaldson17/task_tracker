from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Simple in-memory storage (resets on each deployment)
tasks = []
task_counter = 1

class TaskForm(FlaskForm):
    title = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')

@app.route('/', methods=['GET', 'POST'])
def index():
    global task_counter
    form = TaskForm()
    
    if form.validate_on_submit():
        task = {
            'id': task_counter,
            'title': form.title.data,
            'completed': False,
            'created_at': datetime.utcnow()
        }
        tasks.append(task)
        task_counter += 1
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form, tasks=tasks)

@app.route('/toggle/<int:id>')
def toggle_task(id):
    for task in tasks:
        if task['id'] == id:
            task['completed'] = not task['completed']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)