"""
Fetch solutions.
"""

import argparse

from tools.fetch_discussion import fetch_discussion
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


def main():
    args = parse_args()
    candidates = read_json(args.file)

    for cand in candidates:
        if cand['rank'] is None:
            continue
        rank_str = ordinalize(cand['rank'])
        title = f'{rank_str} place solution'
        fetch_discussion(cand['url'], title)


if __name__ == '__main__':
    main()
