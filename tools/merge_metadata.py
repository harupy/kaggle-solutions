"""
Merge competition metadata.
"""

import os
import re
from tqdm import tqdm

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
    """
    solutions = [read_json(os.path.join(directory, fn)) for fn in os.listdir(directory)]
    # Assert the competition slug equals to the directory name.
    comp_slug = os.path.basename(os.path.dirname(directory))
    assert all(parse_competition_slug(sol['url']) == comp_slug for sol in solutions)

    # Use discussion id to make the order of solutions becomes non-deterministic
    # when some solutions have the same rank.
    solutions.sort(key=lambda sol: (parse_rank(sol['title']), sol['discussionId']))
    return solutions


def merge_metadata():
    meta_all = []
    comps = os.listdir(COMPETITIONS_DIR)

    for comp_slug in tqdm(comps):
        comp_dir = os.path.join(COMPETITIONS_DIR, comp_slug)

        if not os.path.isdir(comp_dir):
            continue

        comp_meta = read_json(os.path.join(comp_dir, 'metadata.json'))

        solutions_dir = os.path.join(comp_dir, SOLUTIONS_DIR)
        if os.path.exists(solutions_dir):
            solutions = read_solutions(solutions_dir)
            comp_meta['solutions'] = solutions

        meta_all.append(comp_meta)

    meta_all.sort(key=lambda m: (m['enabledDate'], m['competitionId']), reverse=True)
    return meta_all


def main():
    meta_all = merge_metadata()
    save_path = os.path.join(CLIENT_SRC_DIR, 'competitions.json')
    to_json(meta_all, save_path)
    print('Saved to:', save_path)


if __name__ == '__main__':
    main()
