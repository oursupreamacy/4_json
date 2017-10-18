import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as json_file:
        parsed_json = json.load(json_file)
    return parsed_json


def pretty_print_json(parsed_json):
    print(json.dumps(parsed_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    filepath = sys.argv[1]
    pretty_print_json(load_data(filepath))

