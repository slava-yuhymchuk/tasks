from flask import Flask, request, abort
import tasks_be

app = Flask(__name__)

# Return all tasks.
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = tasks_be.read_file().get("Tasks",[])
    return tasks

# Return specific task by ID.
@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = next((task for task in get_tasks() if task["ID"] == id), None)
    if task: return task
    else: abort(404)

# Add new task with POST request data. Return newly created task.
@app.route("/tasks", methods=["POST"])
def add_task():
    tasks = get_tasks()
    ids = [0]
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

# Delete specific task by ID. Return deleted task.
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = get_task(id)
    tasks = get_tasks()
    tasks = [task for task in tasks if task["ID"] != id]
    try: tasks_be.write_tasks(tasks)
    except Exception as error: abort(500, error)
    finally: return task

# Update specific task with PUT request data. Return updated task.
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id, title, details):
    pass

# Change the status of specific task to "Done". Return completed task.
@app.route("/tasks/<int:id>/done", methods=["PUT"])
def mark_done(id):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
