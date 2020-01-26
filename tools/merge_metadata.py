"""
Merge competition meta data and save it in the client source directory.
"""

import os
import re

from tools.utils import read_json, to_json
from tools.config import COMPETITIONS_DIR, SOLUTIONS_DIR, CLIENT_SRC_DIR


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
    ...     data = [{'title': '1st'}, {'title': '2nd'}]
    ...     for idx, d in enumerate(data):
    ...         with open(os.path.join(tmpdir, f'{idx}.json'), 'w') as f:
    ...             json.dump(d, f)
    ...     data == read_solutions(tmpdir)
    True

    """
    solutions = [read_json(os.path.join(directory, fn)) for fn in os.listdir(directory)]
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
    print('Saved to', save_path)


if __name__ == '__main__':
    main()
