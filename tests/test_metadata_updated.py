# import unittest

from tools.merge_metadata import merge_metadata
from tools.utils import read_json


def test_metadata_updated():
    metadata_path = 'client/src/competitions.json'
    script_path = 'tools/merge_metadata.py'
    msg = (f'The content of `{metadata_path}` does not equal to '
           f'the result of `{script_path}`. Please run `{script_path}`.')
    actual = read_json(metadata_path)
    # print(len(actual))
    # actual.sort(key=lambda m: m['enabledDate'], reverse=True)
    expected = merge_metadata()
    # print(len(expected))
    # expected.sort(key=lambda m: m['enabledDate'], reverse=True)
    # tc = unittest.TestCase('__init__')
    # tc.assertCountEqual(actual, expected, msg)

    for a, b in zip(actual, expected):
        print(a, b)
        assert a == b, msg
