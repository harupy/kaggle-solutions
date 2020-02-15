"""
Fetch solution candidates.
"""
import argparse
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tools.config import KAGGLE_URL
from tools.utils import make_headless_chrome, make_soup, to_json


def parse_args():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(description='Fetch competition metadata.')
    parser.add_argument('-s', '--slug', required=True, help='Competition slug')
    parser.add_argument('-o', '--overwrite', action='store_true',  # Default value is `False`.
                        help='If specified, overwrite an existing file.')
    return parser.parse_args()


def fetch_solution_candidates(soup):
    """
    Get solution candidates.
    """
    result = []
    for block in soup.select('div.block-link'):
        link = block.select('a.block-link__anchor')[0]
        author = block.select('a.avatar')[0]
        avatar = block.select('img.avatar__thumbnail')[0]

        raw_title = link.get('title')
        if 'solution' not in raw_title.strip().lower():
            continue

        url = KAGGLE_URL + link.get('href')
        author_id = os.path.basename(author.get('href'))
        author_name = avatar.get('alt')
        result.append({
            'rawTitle': raw_title,
            'authorId': author_id,
            'authorName': author_name,
            'title': None,
            'rank': None,
            'url': url}
        )
    return result


def main():
    args = parse_args()
    url = f'https://www.kaggle.com/c/{args.slug}/discussion'
    driver = make_headless_chrome()
    num_scrolls = 2
    sleep_duration = 5

    try:
        driver.get(url)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.smart-list__search')))
        input_box = driver.find_element_by_css_selector('input.smart-list__search')
        input_box.send_keys('solution')
        # TODO: Use wait-until if possible.
        time.sleep(sleep_duration)  # Wait for the search to finish.

        # Scroll to the bottom twice to increase discussions (one scroll adds 20 discussions).
        for i in range(num_scrolls):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            # TODO: Use wait-until if possible.
            time.sleep(sleep_duration)  # Wait for the loading to finish.
        html = driver.page_source
    except Exception as e:
        driver.quite()
        raise e

    soup = make_soup(html)
    candidates = fetch_solution_candidates(soup)
    save_path = os.path.join('solution-candidates', f'{args.slug}.json')

    if not args.overwrite and os.path.exists(save_path):
        raise IOError(f'A file named `{save_path}` already exists. '
                      'If you want to overwrite it, enable `--overwrite` option.')

    to_json(candidates, save_path)
    print('Saved to:', save_path)


if __name__ == '__main__':
    main()
