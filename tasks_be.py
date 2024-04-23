from os import path
from json import load, dump

file_name = "tasks.json"

# Create new empty JSON file.
def create_file():
        json_data = {"Tasks": []}
        write_file(json_data)

# Read the contents of the JSON file.
def read_file():
    # Initialize with and empty JSON file if one still doesn't exist.
    if not path.isfile(file_name):
        create_file()
    json_file = open(file_name,"r")
    json_data = load(json_file)
    json_file.close()
    return json_data

# Overwrite the contents of the JSON file.
def write_file(json_data):
    json_file = open(file_name, "w")
    dump(json_data, json_file, indent=4)
    json_file.close()

# Write tasks to the JSON file.
def write_tasks(tasks):
    json_data = {"Tasks": tasks}
    write_file(json_data)

# if __name__ == "__main__":
    # a = read_file()
    # print (a)