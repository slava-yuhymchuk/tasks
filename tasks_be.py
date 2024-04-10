
import json

json_file = open("tasks.json","r+")
tasks = json.load(json_file)

def get_tasks():
    tasks = json.load(json_file)
    return tasks

def get_task(id):
    tasks = json.load(json_file)
    return tasks[id]

def add_task(task_id,task_name,task_details):
    pass

def delete_task(task_id):
    pass

def update_task(task_id,task_name,task_details):
    pass

#get_task(1)
a = tasks.jsonify('"1": {"title":"buy","details":"milk"}')
a