import Common.constants as serviceConst
import json
from flask import jsonify

def return_existing_data(path):
    # Read the initial JSON data from the file
    with open(path, 'r') as json_file:
        constants_data = json.load(json_file)
    return jsonify(constants_data)

def update_new_data(path, new_constants_data):
    constants_data = None
    
    with open(path, 'r') as json_file:
        constants_data = json.load(json_file)

    if new_constants_data:
        # Update the existing constants_data with new values
        constants_data.update(new_constants_data)

        # Save the updated data to the JSON file
        with open(path, 'w') as json_file:
            json.dump(constants_data, json_file, indent=4)

        return jsonify({"message": "Constants updated successfully"})
    else:
        return jsonify({"error": "Invalid JSON data provided"}), 400

def fetch_value_from_config(path, name):
    with open(path, 'r') as json_file:
        constants_data = json.load(json_file)
        return constants_data[name]