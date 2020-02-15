"""
Fetch all competition metadata.
"""
import math
import os
import time

import requests

from tools.config import COMPETITIONS_DIR
from tools.utils import to_json


def fetch_competitions():
    """
    Fetch all competition metadata from Kaggle.

    Notes
    -----
    This function might cause HTTP error 429 (Too Many Requests).

    """
    comps_all = []
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

        print(f'{page} / {total_pages}', f'(status code: {resp.status_code})')

        comps = data['pagedCompetitionGroup']['competitions']
        if len(comps) == 0:
            break
        comps_all += comps

        time.sleep(SLEEP_DURATION)  # Prevent HTTP error 429.

    return comps_all


def main():
    if not os.path.exists(COMPETITIONS_DIR):
        os.mkdir(COMPETITIONS_DIR)

    comps = fetch_competitions()
    num_comps = len(comps)

    for comp_idx, comp in enumerate(comps):
        print(f'{comp_idx + 1} / {num_comps}')
        comp_name = os.path.basename(comp['competitionUrl'])
        save_dir = os.path.join(COMPETITIONS_DIR, comp_name)

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        save_path = os.path.join(save_dir, 'metadata.json')
        to_json(comp, save_path)


if __name__ == '__main__':
    main()
