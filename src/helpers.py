import json
import os.path

from .settings.common import *


def printt(data, beauty=True):
    if beauty:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print(data)


def save_data_to_file(data_name, data, overwrite = False):
    path = f'{DATA_DIRECTORY}/{data_name}.json'
    is_empty_file = False

    if not os.path.isfile(path):
        is_empty_file = True
        open(path, "a")
        with open(path, "w") as write_file:
            json.dump([], write_file)

    if overwrite or is_empty_file:
        with open(path, "w") as write_file:
            json.dump(data, write_file, indent=2, default=str)
    else:
        print ("Data file already exist or is not empty, set overwrite = TRUE to overwrite contents")


def get_data_from_local(data_name):
    path = f'{DATA_DIRECTORY}/{data_name}.json'

    if os.path.isfile(path):
        with open(path) as json_file:
            return json.load(json_file)
    else:
        print(f'File does not exit at "{path}"')