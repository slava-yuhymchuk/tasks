from flask import Flask, request, abort
import tasks_be

app = Flask(__name__)

# Return all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = tasks_be.read_file().get("Tasks",[])
    return tasks

# Return specific task by ID
@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = next((task for task in get_tasks() if task["ID"] == id), None)
    if task: return task
    else: abort(404)

# Add new task from POST request data
@app.route("/tasks", methods=["POST"])
def add_task():
    tasks = tasks_be.read_file().get("Tasks",[])
    ids = []
    for task in tasks:
        ids.append(task["ID"])
    id = (max(ids))+1
    title = request.json["Title"]
    details = request.json["Details"]
    task = {"ID": id, "Title": title, "Details": details, "Status": "New"}
    tasks.append(task)
    try: tasks_be.write_tasks(tasks)
    except Exception as error: abort(500, error)
    finally: return task

@app.route("/tasks/<int:task_id>", methods=["POST"])
def delete_task(id):
    pass

@app.route("/tasks/<int:task_id>", methods=["POST"])
def update_task(id):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # a = add_task()
    # print (a)