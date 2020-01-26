"""
Fetch solution candidates.
"""

import os
import time
import argparse
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tools.utils import to_json, make_soup, make_headless_chrome
from tools.config import KAGGLE_URL


def parse_args():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(description='Fetch competition metadata.')
    parser.add_argument('-s', '--slug', required=True, help='Competition slug')
    return parser.parse_args()


def get_solution_candidates(soup):
    """
    Get solution candidates.
    """
    result = []
    for link in soup.select('a.block-link__anchor'):
        raw_title = link.get('title')
        if 'solution' not in raw_title.strip().lower():
            continue
        url = KAGGLE_URL + link.get('href')
        result.append({
            'raw_title': raw_title,
            'title': '',
            'rank': None,
            'url': url}
        )
    return result


def main():
    args = parse_args()
    url = f'https://www.kaggle.com/c/{args.slug}/discussion'
    driver = make_headless_chrome()

    try:
        driver.get(url)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.smart-list__search')))
        input_box = driver.find_element_by_css_selector('input.smart-list__search')
        input_box.send_keys('solution')
        time.sleep(5)  # Wait for the search to finish. TODO: Use wait-until.
        # Scroll to the bottom twice to increase discussions.
        for i in range(2):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)  # Wait for the loading to finish.  TODO: Use wait-until.
        html = driver.page_source
    except Exception:
        print(traceback.format_exc())
    finally:
        driver.quit()

    soup = make_soup(html)
    candidates = get_solution_candidates(soup)
    save_path = os.path.join('solution-candidates', f'{args.slug}.json')
    to_json(candidates, save_path)
    print('Saved to:', save_path)


if __name__ == '__main__':
    main()
