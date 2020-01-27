"""
Fetch solutions.
"""

import argparse

from tools.fetch_discussions import fetch_discussions
from tools.utils import read_json


def parse_args():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(description='Fetch discussion metadata.')
    parser.add_argument('-f', '--file', required=True,
                        help='JSON file that contains solution candidates.')
    return parser.parse_args()


def ordinalize(n):
    """
    Ordinalize a number.

    Examples
    --------
    >>> [ordinalize(n) for n in range(1, 4 + 1)]
    ['1st', '2nd', '3rd', '4th']

    """
    mapper = {
        1: 'st',
        2: 'nd',
        3: 'rd',
    }
    return str(n) + mapper.get(n % 10, 'th')


def process_candidates(candidates):
    """
    Make (url, title) pairs.
    """
    result = []
    for cand in candidates:
        if cand['rank'] is None:
            continue
        rank_str = ordinalize(cand['rank'])

        title = cand['title'] or f'{rank_str} place solution'
        result.append((cand['url'], title))
    return result


def main():
    args = parse_args()
    candidates = read_json(args.file)
    items = process_candidates(candidates)
    fetch_discussions(items)


if __name__ == '__main__':
    main()
