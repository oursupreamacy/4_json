# encoding: utf-8
import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as handle:
        parsed = json.load(handle)
    return parsed


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    l = sys.argv[1]
    r = load_data(l)
    pretty_print_json(r)

