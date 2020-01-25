import json


def read_json(fpath):
    """
    Read a JSON file.
    """
    with open(fpath, 'r') as f:
        return json.load(f)


def to_json(d, fpath):
    """
    Save a dict as JSON.
    """
    with open(fpath, 'w') as f:
        json.dump(d, f, indent=2, sort_keys=True)
        f.write('\n')
