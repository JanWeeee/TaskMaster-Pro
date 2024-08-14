from flask import Blueprint, jsonify, request, abort, session
from api.models import Task, db_session
from datetime import datetime

tasks_api = Blueprint('tasks_api', __name__)

@tasks_api.route('/tasks', methods=['GET'])
def get_tasks():
    user_id = session.get('user_id')
    if not user_id:
        abort(401)
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_api.route('/tasks', methods=['POST'])
def create_task():
    user_id = session.get('user_id')
    if not user_id:
        abort(401)
    data = request.json
    due_date = datetime.strptime(data['due_date'], '%Y-%m-%dT%H:%M')
    task = Task(title=data['title'], description=data['description'], due_date=due_date, user_id=user_id)
    db_session.add(task)
    db_session.commit()
    return jsonify(task.to_dict()), 201

@tasks_api.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    user_id = session.get('user_id')
    if not user_id:
        abort(401)
    task = Task.query.get(id)
    if not task or task.user_id != user_id:
        abort(404)
    data = request.json
    task.title = data['title']
    task.description = data['description']
    task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%dT%H:%M')
    db_session.commit()
    return jsonify(task.to_dict())

@tasks_api.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    user_id = session.get('user_id')
    if not user_id:
        abort(401)
    task = Task.query.get(id)
    if not task or task.user_id != user_id:
        abort(404)
    db_session.delete(task)
    db_session.commit()
    return '', 204

@tasks_api.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    user_id = session.get('user_id')
    if not user_id:
        abort(401)
    task = Task.query.get(id)
    if not task or task.user_id != user_id:
        abort(404)
    return jsonify(task.to_dict())
