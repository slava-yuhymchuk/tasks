# v1.0
from flask import Flask, request, make_response, abort
from os import path
from json import load, dump

app = Flask(__name__)

file_name = "tasks.json"

# Create new empty JSON file.
@app.route("/be/create_file", methods=["POST"])
def create_file():
    json_data = {"Tasks": []}
    try: 
        write_file(json_data)
        return make_response("",200)
    except Exception as error: abort(500, error)

# Read the contents of the JSON file.
@app.route("/be/read_file", methods=["GET"])
def read_file():
    # Initialize with an empty JSON file if one still doesn't exist.
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
@app.route("/be/write_tasks", methods=["POST"])
def write_tasks():
    tasks = request.json
    json_data = {"Tasks": tasks}
    try: 
        write_file(json_data)
        return make_response("",200)
    except Exception as error: abort(500, error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
