# v2.77
from flask import Flask, request, abort, render_template, jsonify
from os import environ
import requests
import tasks_ai

app = Flask(__name__)

BE_URL = environ["BE_URL"]
FE_PORT = environ["FE_PORT"]

@app.route("/")
def home():
    return render_template('index.html')

# Return all tasks.
@app.route("/tasks", methods=["GET"])
def get_tasks():
    URL = BE_URL + "/read_file"
    response = requests.get(URL).json()
    tasks = response.get("Tasks",[])
    return jsonify(tasks=tasks)

# Return specific task by ID.
@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    URL = BE_URL + "/read_file"
    response = requests.get(URL).json()
    tasks = response.get("Tasks",[])
    task = next((task for task in tasks if task["ID"] == id), None)
    if task: return task
    else: abort(404)

# Add new task with POST request data. Return newly created task.
@app.route("/tasks", methods=["POST"])
def add_task():
    URL = BE_URL + "/read_file"
    response = requests.get(URL).json()
    tasks = response.get("Tasks", [])
    ids = [0]
    for task in tasks:
        ids.append(task["ID"])
    id = max(ids) + 1
    title = request.json["Title"]
    details = request.json["Details"]
    task = {"ID": id, "Title": title, "Details": details, "Status": "New"}
    tasks.append(task)
    URL = BE_URL + "/write_tasks"
    headers = {"Content-Type": "application/json"}
    try: 
        requests.post(URL, headers=headers, json=tasks)
        return jsonify(task)
    except Exception as error: 
        abort(500, description=str(error))

# Delete specific task by ID. Return deleted task.
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = get_task(id)
    if not task:
        abort(404, description="Task not found")
    URL = BE_URL + "/read_file"
    response = requests.get(URL).json()
    tasks = response.get("Tasks", [])
    tasks = [task for task in tasks if task["ID"] != id]
    URL = BE_URL + "/write_tasks"
    headers = {"Content-Type": "application/json"}
    try: 
        requests.post(URL, headers=headers, json=tasks)
        return jsonify({"message": "Task deleted successfully"})
    except Exception as error: 
        abort(500, description=str(error))

# Update specific task with PUT request data. Return updated task.
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = get_task(id)
    URL = BE_URL + "/read_file"
    response = requests.get(URL).json()
    tasks = response.get("Tasks", [])
    title = request.json["Title"]
    details = request.json["Details"]
    status = request.json.get("Status", task["Status"])
    updated_task = {"ID": id, "Title": title, "Details": details, "Status": status}
    tasks[tasks.index(task)] = updated_task
    URL = BE_URL + "/write_tasks"
    headers = {"Content-Type": "application/json"} 
    try: 
        requests.post(URL, headers=headers, json=tasks)
        return updated_task
    except Exception as error: 
        abort(500, error)

# Change the status of specific task to "Done". Return completed task.
@app.route("/tasks/<int:id>/done", methods=["POST"])
def mark_done(id):
    task = get_task(id)
    if not task:
        abort(404, description="Task not found")
    URL = BE_URL + "/read_file"
    response = requests.get(URL).json()
    tasks = response.get("Tasks", [])
    completed_task = {"ID": task["ID"], "Title": task["Title"], "Details": task["Details"], "Status": "Done"}
    tasks[tasks.index(task)] = completed_task
    URL = BE_URL + "/write_tasks"
    headers = {"Content-Type": "application/json"} 
    try: 
        requests.post(URL, headers=headers, json=tasks)
        return jsonify(completed_task)
    except Exception as error: 
        abort(500, description=str(error))

# Start over. Return empty task list.
@app.route("/tasks/reset", methods=["POST"])
def reset():
    URL = BE_URL + "/create_file"
    try: 
        requests.post(URL)
        return get_tasks()
    except Exception as error: abort(500, error)

# Ask ChatGPT to assist with specific task. ;)
@app.route("/tasks/<int:id>/ai", methods=["GET"])
def ai(id):
    prompt = get_task(id)["Title"] + " " + get_task(id)["Details"]
    try: return tasks_ai.chatgpt(prompt)
    except Exception as error: abort(400, error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=FE_PORT, ssl_context=("/tasks/tls-crt/tls.crt", "/tasks/tls-key/tls.key"))
