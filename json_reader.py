import json


def read_json_file(self, file_path: str):
    with open(file_path) as json_file:
        json_string = json_file.read()
        # convert json string into python variable
        data = json.loads(json_string)
        return data


def write_json_file(self, file_path: str, data):
    # convert python variable into json string
    json_string = json.dumps(data, indent=4, sort_keys=True)
    # write json string into file
    with open(file_path, "w") as file:
        file.write(json_string)
