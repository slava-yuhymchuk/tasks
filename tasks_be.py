import os
import json

file_name = "tasks.json"

def create_file():
    if not os.path.isfile(file_name):
        json_data = {"Tasks": []}
        json_file = open(file_name, "w")
        json.dump(json_data, json_file, indent=4)
        json_file.close()

def read_file():
    create_file()
    json_file = open(file_name,"r")
    json_data = json.load(json_file)
    json_file.close()
    return json_data

def write_file(tasks):
    json_data = {"Tasks": tasks}
    json_file = open(file_name, "w")
    json.dump(json_data, json_file, indent=4)
    json_file.close() 
    
def delete_task(task_id):
    pass

def update_task(task_id,task_name,task_details):
    pass

if __name__ == "__main__":
    a = read_file()
    print (a)

#a = tasks.jsonify('"1": {"title":"buy","details":"milk"}')
#a