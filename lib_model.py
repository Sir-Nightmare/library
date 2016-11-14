import json

NUMBER_OF_userS_FOR_USER = 3


def load_data_from_json(file_path):
    with open(file_path, 'r') as input_file:
        return json.load(input_file)


def write_data_to_json(data_to_write, file_path):
    with open(file_path, 'w') as file_to_write:
        json.dump(data_to_write, file_to_write, indent=4, sort_keys=True, ensure_ascii=False)
