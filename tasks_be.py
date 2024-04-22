import os
import json

file_name = "tasks.json"

def create_file():
    if not os.path.isfile(file_name):
        json_file = open(file_name, "w")
        json.dump({"tasks": []}, json_file)
        json_file.close()

def read_file():
    create_file()
    json_file = open(file_name,"r")
    json_data = json.load(json_file)
    json_file.close()
    return json_data

def get_tasks():
    tasks = read_file().get("tasks",[])
    return tasks

def get_task(id):
    task = next((task for task in get_tasks() if task["id"] == id), None)
    return task
    #return jsonify(task.to_json())

def add_task(task_id,task_name,task_details):
    pass

def delete_task(task_id):
    pass

def update_task(task_id,task_name,task_details):
    pass

if __name__ == "__main__":
    a = get_tasks()
    print (a)

#a = tasks.jsonify('"1": {"title":"buy","details":"milk"}')
#a