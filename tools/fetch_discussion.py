"""
Fetch discussion meta data.
"""

import os
import argparse
import traceback
import re
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils import to_json

# Please download if you don't have ChromeDriver from the link below.
# https://chromedriver.chromium.org/downloads
options = Options()
options.add_argument('--headless')
driver = Chrome('./chromedriver', options=options)


def parse_args():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(description='Extract metadata of a discussion.')
    parser.add_argument('-u', '--url', required=True, help='Discussion URL')
    parser.add_argument('-t', '--title',
                        help='If specified, use this title instead of a scraped title.')
    return parser.parse_args()


def format_solution_title(title):
    """
    Format a solution title.
    """
    pattern = r'^\d+[a-zA-Z]{2} [pP]lace [sS]olution'  # e.g.: 1st place solution
    m = re.match(pattern, title)
    matched = m.group(0)
    return title.replace(matched, matched.lower())


def validate_solution_title(title):
    """
    Raise ValueError if title doesn't follow the specified format.
    """
    pattern = r'^\d+[a-z]{2} place solution'  # e.g.: 1st place solution
    m = re.match(pattern, title)
    if m is None:
        raise ValueError('Solution title "{}" is not acceptable.'.format(title))


def make_soup(html):
    """
    Instantiate a soup object.
    """
    return BeautifulSoup(html, 'lxml')


def get_discussion_id(url):
    """
    Get a discussion id.
    """
    return os.path.basename(url)


def get_competition_slug(url):
    """
    Get a competition slug.
    """
    pattern = r'^https://www.kaggle.com/c/(.+?)/'
    m = re.match(pattern, url)
    return m.group(1)


def get_avatar_image(soup):
    """
    Parse an avatar source.
    """
    pattern = r'^https://storage.googleapis.com/kaggle-avatars/(.+)'
    img = soup.find('img', {'src': re.compile(pattern)})
    return os.path.basename(img.get('src'))


def get_author_name_and_id(soup):
    """
    Get author name and id.
    """
    author = soup.select('a.topic__author-link')[0]
    return author.text.strip(), author.get('href').strip('/')


def get_title(soup):
    """
    Get a topic title.
    """
    return soup.find('title').text.split('|')[0].strip()


def main():
    args = parse_args()
    url = args.url
    comp_slug = get_competition_slug(url)
    discussion_id = get_discussion_id(url)

    try:
        driver.get(url)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.comment-list')))
        html = driver.page_source
    except Exception:
        print(traceback.format_exc())
    finally:
        driver.quit()

    soup = make_soup(html)
    raw_title = get_title(soup)
    title = args.title or raw_title
    title = format_solution_title(title)
    validate_solution_title(title)

    avatar_image = get_avatar_image(soup)
    author_name, author_id = get_author_name_and_id(soup)
    data = {
        'raw_title': raw_title,
        'title': title,
        'discussionId': discussion_id,
        'authorName': author_name,
        'authorId': author_id,
        'avatarImage': avatar_image,
        "url": url,
    }

    save_path = os.path.join('competitions/{}/solutions/{}_{}.json'
                             .format(comp_slug, author_id, discussion_id))
    to_json(data, save_path)
    print('\nSaved to', save_path)


if __name__ == '__main__':
    main()
