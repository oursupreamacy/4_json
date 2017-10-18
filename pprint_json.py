import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as handle:
        parsed = json.load(handle)
    return parsed


def pretty_print_json(parsed):
    print(json.dumps(parsed, indent=4, sort_keys=True))


if __name__ == '__main__':
    filepath = sys.argv[1]
    pretty_print_json(load_data(filepath))

