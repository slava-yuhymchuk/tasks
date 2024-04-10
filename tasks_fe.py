
from flask import Flask, request

import json
import tasks_be

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return json.dumps(tasks_be.tasks)

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    return tasks_be.tasks[id]

@app.route("/tasks", methods=["POST"])
def add_task():
    new_task = request.data
    tasks_be.add_task(new_task)
    return json.dumps(new_task)

@app.route("/tasks/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    pass

@app.route("/tasks/<int:task_id>", methods=["POST"])
def update_task(task_id):
    pass