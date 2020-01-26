"""
Merge competition metadata.
"""

import os
import re

from tools.utils import read_json, to_json
from tools.config import COMPETITIONS_DIR, SOLUTIONS_DIR, CLIENT_SRC_DIR


def parse_competition_slug(url):
    """
    Parse a competition slug from given URL.

    Examples
    --------
    >>> parse_competition_slug('https://www.kaggle.com/c/titanic/discussion/1234')
    'titanic'

    >>> parse_competition_slug('https://www.kaggle.com/c/titanic')
    'titanic'

    >>> parse_competition_slug('https://www.kaggle.com/c/titanic/')
    'titanic'

    """
    pattern = r'^https://www.kaggle.com/c/([^/]+)'
    m = re.match(pattern, url)
    return m.group(1)


def parse_rank(solution_title):
    """
    Parse a rank from a solution title.

    Examples
    --------
    >>> parse_rank('1st solution title')
    1

    >>> parse_rank('21st solution title')
    21

    """
    m = re.match(r'^(\d+)', solution_title)
    return int(m.group(1))


def read_solutions(directory):
    """
    Read solutions in the given directory.

    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     slug = os.path.basename(os.path.dirname(tmpdir))
    ...     url = 'https://www.kaggle.com/c/{}'.format(slug)
    ...     data = [{'title': '1st', 'url': url},
    ...             {'title': '2nd', 'url': url}]
    ...     for idx, d in enumerate(data):
    ...         with open(os.path.join(tmpdir, f'{idx}.json'), 'w') as f:
    ...             json.dump(d, f)
    ...     data == read_solutions(tmpdir)
    True

    """
    solutions = [read_json(os.path.join(directory, fn)) for fn in os.listdir(directory)]
    # Assert the competition slug equals to the directory name.
    comp_slug = os.path.basename(os.path.dirname(directory))
    assert all(parse_competition_slug(sol['url']) == comp_slug for sol in solutions)
    solutions.sort(key=lambda sol: parse_rank(sol['title']))
    return solutions


def merge_metadata():
    meta_all = []
    comps = os.listdir(COMPETITIONS_DIR)
    num_comps = len(comps)

    for comp_idx, comp_slug in enumerate(comps):
        print(f'{comp_idx + 1} / {num_comps}')
        comp_dir = os.path.join(COMPETITIONS_DIR, comp_slug)

        if not os.path.isdir(comp_dir):
            continue

        comp_meta = read_json(os.path.join(comp_dir, 'metadata.json'))

        solutions_dir = os.path.join(comp_dir, SOLUTIONS_DIR)
        if os.path.exists(solutions_dir):
            solutions = read_solutions(solutions_dir)
            comp_meta['solutions'] = solutions

        meta_all.append(comp_meta)

    meta_all.sort(key=lambda m: m['enabledDate'], reverse=True)
    return meta_all


def main():
    meta_all = merge_metadata()
    save_path = os.path.join(CLIENT_SRC_DIR, 'competitions.json')
    to_json(meta_all, save_path)
    print('Saved to:', save_path)


if __name__ == '__main__':
    main()
