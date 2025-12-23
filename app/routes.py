from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Task
from app.forms import TaskForm

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    tasks = Task.query.all()
    return render_template('index.html', form=form, tasks=tasks)

@bp.route('/toggle/<int:id>')
def toggle_task(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))