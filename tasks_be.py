from os import path
from json import load, dump

file_name = "tasks.json"

# Initialize with an empty JSON file if one still doesn't exist
def create_file():
    if not path.isfile(file_name):
        json_data = {"Tasks": []}
        write_file(json_data)

# Read the contents of the JSON file
def read_file():
    create_file()
    json_file = open(file_name,"r")
    json_data = load(json_file)
    json_file.close()
    return json_data

# Overwrite the contents of the JSON file
def write_file(json_data):
    json_file = open(file_name, "w")
    dump(json_data, json_file, indent=4)
    json_file.close()

# Write tasks to the JSON file
def write_tasks(tasks):
    json_data = {"Tasks": tasks}
    write_file(json_data)

def delete_task(task_id):
    pass

def update_task(task_id,task_name,task_details):
    pass

if __name__ == "__main__":
    a = read_file()
    print (a)

#a = tasks.jsonify('"1": {"title":"buy","details":"milk"}')
#a