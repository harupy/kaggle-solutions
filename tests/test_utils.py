import json
import os

from tools import utils


def test_to_json(tmpdir):
    data = {'a': 0}
    fpath = os.path.join(tmpdir, 'data.json')
    utils.to_json(data, fpath)
    assert os.path.exists(fpath)


def test_read_json(tmpdir):
    data = {'a': 0}
    fpath = os.path.join(tmpdir, 'data.json')
    with open(fpath, 'w') as f:
        json.dump(data, f)
    assert data == utils.read_json(fpath)
