import json


def read_json(fpath):
    """
    Read a JSON file.

    Examples
    --------
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     data = {'a': 0}
    ...     fpath = os.path.join(tmpdir, 'data.json')
    ...     with open(fpath, 'w') as f:
    ...         json.dump(data, f)
    ...     data == read_json(fpath)
    True

    """
    with open(fpath, 'r') as f:
        return json.load(f)


def to_json(data, fpath):
    """
    Save a dict as JSON.

    Examples
    --------
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     data = {'a': 0}
    ...     fpath = os.path.join(tmpdir, 'data.json')
    ...     to_json(data, fpath)
    ...     os.path.exists(fpath)
    True

    """
    with open(fpath, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write('\n')
