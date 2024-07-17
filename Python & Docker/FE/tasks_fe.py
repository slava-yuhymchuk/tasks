from flask import Flask, request, abort, render_template, jsonify
import requests
import tasks_ai

app = Flask(__name__)

# BE_URL = "http://localhost:5000/be"a
BE_URL = "http://tasks-be:5000/be"

@app.route("/")
def index():
    return render_template("index.html")

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
    URL = BE_URL + "/write_tasks"
    headers = {"Content-Type": "application/json"}
    try: 
        requests.post(URL, headers=headers, json=tasks)
        return task
    except Exception as error: abort(500, error)

# Delete specific task by ID. Return deleted task.
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = get_task(id)
    tasks = get_tasks()
    tasks = [task for task in tasks if task["ID"] != id]
    URL = BE_URL + "/write_tasks"
    headers = {"Content-Type": "application/json"}
    try: 
        requests.post(URL, headers=headers, json=tasks)
        return task
    except Exception as error: abort(500, error)

# Update specific task with PUT request data. Return updated task.
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = get_task(id)
    tasks = get_tasks()
    title = request.json["Title"]
    details = request.json["Details"]
    status = request.json["Status"]
    updated_task = {"ID": id, "Title": title, "Details": details, "Status": status}
    tasks[tasks.index(task)] = updated_task
    URL = BE_URL + "/write_tasks"
    headers = {"Content-Type": "application/json"} 
    try: 
        requests.post(URL, headers=headers, json=tasks)
        return updated_task
    except Exception as error: abort(500, error)

# Change the status of specific task to "Done". Return completed task.
@app.route("/tasks/<int:id>/done", methods=["POST"])
def mark_done(id):
    task = get_task(id)
    tasks = get_tasks()
    completed_task = {"ID": task["ID"], "Title": task["Title"], "Details": task["Details"], "Status": "Done"}
    tasks[tasks.index(task)] = completed_task
    URL = BE_URL + "/write_tasks"
    headers = {"Content-Type": "application/json"} 
    try: 
        requests.post(URL, headers=headers, json=tasks)
        return completed_task
    except Exception as error: abort(500, error)

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
    app.run(host="0.0.0.0", port=80)
