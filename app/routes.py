from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.models import Task
from app.forms import TaskForm
from app import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', form=form, tasks=tasks)

@main.route('/task/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return jsonify({'success': True, 'completed': task.completed})

@main.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'success': True})

@main.route('/task/<int:task_id>/edit', methods=['POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    new_title = request.json.get('title', '').strip()
    
    if new_title:
        task.title = new_title
        db.session.commit()
        return jsonify({'success': True})
    
    return jsonify({'success': False, 'error': 'Title cannot be empty'})

@main.route('/tasks/clear-completed', methods=['POST'])
def clear_completed():
    Task.query.filter_by(completed=True).delete()
    db.session.commit()
    return jsonify({'success': True})