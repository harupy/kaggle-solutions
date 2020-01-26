"""
Fetch competition metadata.
"""

import os
import time
import math
import argparse
import requests

from tools.utils import to_json
from tools.config import COMPETITIONS_DIR


def parse_args():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(description='Fetch competition metadata.')
    parser.add_argument('-s', '--slug', required=True, help='Competition slug')
    return parser.parse_args()


def find_competition(slug):
    """
    Find a competition that matches the specified slug.

    Notes
    -----
    This function might cause HTTP error 429 (Too Many Requests).

    """
    page = 0
    PAGE_SIZE = 20
    SLEEP_DURATION = 5  # second(s)

    base_url = 'https://www.kaggle.com/competitions.json?sortBy=recentlyCreated&page={}'

    while True:
        page += 1
        resp = requests.get(base_url.format(page))
        data = resp.json()

        if page == 1:
            total_comps = data['pagedCompetitionGroup']['totalCompetitions']
            total_pages = math.ceil(total_comps / PAGE_SIZE)

        print('Processing', f'{page} / {total_pages}', f'(status code: {resp.status_code})')

        comps = data['pagedCompetitionGroup']['competitions']

        for comp in comps:
            if comp['competitionUrl'].endswith(slug):
                print(f"Found a competition: {comp['competitionTitle']}")
                return comp

        if len(comps) == 0:
            break

        time.sleep(SLEEP_DURATION)  # Prevent HTTP error 429.

    raise ValueError(f'Did not find a competition that matches `{slug}`')


def main():
    args = parse_args()

    if not os.path.exists(COMPETITIONS_DIR):
        os.mkdir(COMPETITIONS_DIR)

    comp = find_competition(args.slug.strip())
    comp_name = os.path.basename(comp['competitionUrl'])
    save_dir = os.path.join(COMPETITIONS_DIR, comp_name)

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    save_path = os.path.join(save_dir, 'metadata.json')
    to_json(comp, save_path)
    print('Saved to:', save_path)


if __name__ == '__main__':
    main()
