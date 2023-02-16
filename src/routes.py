from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from src.models import Task
from src import db

tasks = Blueprint('tasks', __name__)


@tasks.route('/')
@tasks.route('/task')
def allTasks():
    """Gets all tasks in the database.
    Args:
    
    Returns:
        (dict): All Tasks in the database.
    """
    all_tasks = Task.query.all()
    return jsonify(Tasks=[task.todict() for task in all_tasks]), 200

@tasks.route('/task/completed')
def completedTask():
    """Gets all tasks that is marked as done in the database.
    Args:
    
    Returns:
        (dict): All Tasks in the database that is marked as done.
    """
    tasks = Task.query.filter(Task.task_is_complete == 1).all()
    return jsonify(completed_tasks=[task.todict() for task in tasks]), 200


@tasks.route('/task', methods=['POST'])
def createTask():
    """Creates a new task in the database.
    Args:
        
    Returns:
        (str): Task created successfully.
    """
    try:
        requestBody = request.get_json()
    except BadRequest:
        return {'error': 'Request body is empty',}, 400

    if not requestBody.get('name') or not requestBody.get('id'):
        return {'error': 'Request body is invalid',}, 400
    
    id = requestBody.get('id')
    name = requestBody.get('name')
    new_task = Task(task_id=id,task_name=name)
    db.session.add(new_task)
    db.session.commit()
    return {'message': 'Task created successfully!'}, 201

@tasks.route('/task/<int:task_id>', methods=['PATCH'])
def updateTask(task_id):
    """Update tasks in the database based on the task_id provided by the user.
    Args:
        task_id (str): This is the TaskID provided by the user in the link.

    Returns:
        json['message']: Task updated successfully.
        json['error']: Request body is empty.
        json['error']: Task not found. Failed to update.
    """
    try:
        requestBody = request.get_json()
    except BadRequest:
        return  {'error': 'Request body is empty.',}, 400

    if not requestBody.get('name') or not requestBody.get('is_complete'):
        return {'error': 'Request body is invalid',}, 400
    
    name = requestBody.get('name')
    is_complete = requestBody.get('is_complete')
    
    if not Task.query.filter(Task.task_id == task_id).update({
        'task_name': name,
        'task_is_complete': is_complete
    }):
        return {'error': 'Task not found. Failed to update.',}, 404
    db.session.commit()
    return {'message': 'Task updated successfully!',} , 202


@tasks.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Deletes the task by the task_id provided by the user.
    Args:
        task_id (str): _description_
        db: Session object where cinacall niya yung database.
    Raises:
        HTTPException: 404 -> wala pong ganyang task.
    Returns:
        json['message']: Task deleted successfully.
        json['error']: Task not found. Failed to delete.
    """
    if not Task.query.filter(Task.task_id == task_id,).delete():
        return {'error': 'Task not found. Failed to delete.', }, 404
    db.session.commit()
    return  {'message': 'Task deleted successfully!', }, 202
