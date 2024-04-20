from flask import *
import json

json_file = open("tasks.json","r+")
json_data = json.load(json_file)
tasks = json_data.get("tasks",[])

def get_tasks():
    json_file = open("tasks.json","r+")
    json_data = json.load(json_file)
    tasks = json_data.get("tasks",[])
    return tasks

def get_task(task_id):
    json_file = open("tasks.json","r+")
    json_data = json.load(json_file)
    tasks = json_data.get("tasks",[])
    task = next((task for task in tasks if task['id'] == task_id), None)
    #print (task)
    return task
    #return jsonify(task.to_json())

def add_task(task_id,task_name,task_details):
    pass

def delete_task(task_id):
    pass

def update_task(task_id,task_name,task_details):
    pass

if __name__ == "__main__":
    a = get_task(1)
    print (a)

#a = tasks.jsonify('"1": {"title":"buy","details":"milk"}')
#a