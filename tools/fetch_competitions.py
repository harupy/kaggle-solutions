"""
Fetch competion meta data.
"""

import os
import requests

from tools.utils import to_json


PARENT_DIR = 'competitions'


def fetch_competitions():
    """
    Fetch all the compeditions from Kaggle.
    """
    comps_all = []
    page = 1
    while True:
        base_url = 'https://www.kaggle.com/competitions.json?sortBy=latestDeadline&group=general&page={}&pageSize=20&category=featured'.format(page)  # noqa
        page += 1

        r = requests.get(base_url)
        comps = r.json()['pagedCompetitionGroup']['competitions']
        comps_all += comps
        if len(comps) == 0:
            break

    return comps_all


def main():
    if not os.path.exists(PARENT_DIR):
        os.mkdir(PARENT_DIR)

    comps = fetch_competitions()
    num_comps = len(comps)

    for comp_idx, comp in enumerate(comps):
        print(f'{comp_idx + 1} / {num_comps}')
        comp_name = os.path.basename(comp['competitionUrl'])
        save_dir = os.path.join(PARENT_DIR, comp_name)

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        fpath = os.path.join(save_dir, 'metadata.json')
        to_json(comp, fpath)


if __name__ == '__main__':
    main()
