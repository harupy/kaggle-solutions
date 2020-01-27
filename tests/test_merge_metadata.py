import os
import json

from tools import merge_metadata as mm


def test_merge_metadata(tmpdir):
    slug = os.path.basename(os.path.dirname(tmpdir))
    url = 'https://www.kaggle.com/c/{}'.format(slug)
    data = [{'title': '1st', 'url': url, 'discussionId': 1},
            {'title': '2nd', 'url': url, 'discussionId': 2}]
    for idx, d in enumerate(data):
        with open(os.path.join(tmpdir, f'{idx}.json'), 'w') as f:
            json.dump(d, f)
    assert data == mm.read_solutions(tmpdir)
