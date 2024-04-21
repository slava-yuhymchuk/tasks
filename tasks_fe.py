
from flask import Flask, request

import json
import tasks_be

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return json.dumps(tasks_be.tasks)

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    return tasks_be.get_task(id)

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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')