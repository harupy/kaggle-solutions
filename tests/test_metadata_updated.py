from pprint import pprint
from tools.merge_metadata import merge_metadata
from tools.utils import read_json


def test_metadata_updated():
    metadata_path = 'client/src/competitions.json'
    script_path = 'tools/merge_metadata.py'
    msg = (f'The content of `{metadata_path}` does not equal to '
           f'the result of `{script_path}`. Please run `{script_path}`.')
    actual = read_json(metadata_path)
    expected = merge_metadata()
    assert expected == actual, msg
