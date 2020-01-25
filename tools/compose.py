"""
Compose competion meta data.
"""

import os
import re

from utils import read_json, to_json


def parse_rank(solution_title):
    """
    Parse a rank from a solution title..
    """
    m = re.match(r'^(\d+)', solution_title)
    return int(m.group(1))


def read_solutions(directory):
    """
    Read solutions in the given directory.
    """
    solutions = [read_json(os.path.join(directory, fn)) for fn in os.listdir(directory)]
    solutions.sort(key=lambda sol: parse_rank(sol['title']))
    return solutions


def main():
    ROOT_DIR = 'competitions'

    meta_all = []
    comps = os.listdir(ROOT_DIR)
    num_comps = len(comps)

    for comp_idx, comp_slug in enumerate(comps):
        print(f'{comp_idx + 1} / {num_comps}')
        comp_dir = os.path.join(ROOT_DIR, comp_slug)

        if not os.path.isdir(comp_dir):
            continue

        comp_meta = read_json(os.path.join(comp_dir, 'metadata.json'))

        solutions_dir = os.path.join(comp_dir, 'solutions')
        if os.path.exists(solutions_dir):
            solutions = read_solutions(solutions_dir)
            comp_meta['solutions'] = solutions

        meta_all.append(comp_meta)

    meta_all.sort(key=lambda m: m['enabledDate'], reverse=True)
    save_path = os.path.join('client/src', 'competitions.json')
    to_json(meta_all, save_path)
    print('Saved to', save_path)


if __name__ == '__main__':
    main()
