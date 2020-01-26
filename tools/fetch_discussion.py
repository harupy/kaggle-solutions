"""
Fetch discussion metadata.
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

from tools.utils import to_json
from tools.config import COMPETITIONS_DIR, SOLUTIONS_DIR


def parse_args():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(description='Fetch discussion metadata.')
    parser.add_argument('-u', '--url', required=True, help='Discussion URL')
    parser.add_argument('-t', '--title',
                        help='Title to display on the UI.')
    return parser.parse_args()


def format_solution_title(title):
    """
    Format a solution title.

    Examples
    --------
    >>> format_solution_title('1st Place Solution')
    '1st place solution'

    >>> format_solution_title('1st Place Solution (part 1)')
    '1st place solution (part 1)'

    """
    pattern = r'^\d+[a-zA-Z]{2} [pP]lace [sS]olution'  # e.g.: 1st place solution
    m = re.match(pattern, title)
    matched = m.group(0)
    return title.replace(matched, matched.lower())


def validate_solution_title(title):
    """
    Raise ValueError if title doesn't follow the specified format.

    Examples
    --------
    >>> validate_solution_title('1st place solution')
    >>> validate_solution_title('1st Place Solution')
    Traceback (most recent call last):
        ...
    ValueError: Solution title "1st Place Solution" is not acceptable.
    """
    pattern = r'^\d+[a-z]{2} place solution'  # e.g.: 1st place solution
    m = re.match(pattern, title)
    if m is None:
        raise ValueError('Solution title "{}" is not acceptable.'.format(title))


def make_soup(html):
    """
    Instantiate a soup object.

    Examples
    --------
    >>> html = '<html><body><h1>header</h1></body></html>'
    >>> make_soup(html)
    <html><body><h1>header</h1></body></html>

    """
    return BeautifulSoup(html, 'lxml')


def get_discussion_id(url):
    """
    Get a discussion id.

    Examples
    --------
    >>> url = 'https://www.kaggle.com/c/titanic/discussion/123456'
    >>> get_discussion_id(url)
    123456

    """
    return int(os.path.basename(url))


def get_competition_slug(url):
    """
    Get a competition slug.

    Examples
    --------
    >>> url = 'https://www.kaggle.com/c/titanic/discussion/1234'
    >>> get_competition_slug(url)
    'titanic'

    """
    pattern = r'^https://www.kaggle.com/c/(.+?)/'
    m = re.match(pattern, url)
    return m.group(1)


def get_avatar_image(soup):
    """
    Parse an avatar source.

    Examples
    --------
    >>> img_tag = '<img src="https://storage.googleapis.com/kaggle-avatars/thumbnails/256794-kg.jpg">'  # noqa
    >>> soup = make_soup(img_tag)
    >>> get_avatar_image(soup)
    '256794-kg.jpg'

    """
    pattern = r'^https://storage.googleapis.com/kaggle-avatars/(.+)'
    img = soup.find('img', {'src': re.compile(pattern)})
    return os.path.basename(img.get('src'))


def get_author_name_and_id(soup):
    """
    Get author name and id.

    Examples
    --------
    >>> a_tag = '<a class="topic__author-link" href="/author_id">author_name</a>'
    >>> soup = make_soup(a_tag)
    >>> get_author_name_and_id(soup)
    ('author_name', 'author_id')

    """
    author = soup.select('a.topic__author-link')[0]
    return author.text.strip(), author.get('href').strip('/')


def get_title(soup):
    """
    Get a topic title.

    Examples
    --------
    >>> title_tag = '<title>title</title>'
    >>> soup = make_soup(title_tag)
    >>> get_title(soup)
    'title'

    """
    return soup.find('title').text.split('|')[0].strip()


def main():
    # Please download ChromeDriver from the link below if you don't have one.
    # https://chromedriver.chromium.org/downloads
    options = Options()
    options.add_argument('--headless')
    driver = Chrome('./chromedriver', options=options)

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

    save_path = os.path.join(COMPETITIONS_DIR,
                             comp_slug,
                             SOLUTIONS_DIR,
                             f'{author_id}_{discussion_id}.json')
    to_json(data, save_path)
    print('\nSaved to', save_path)


if __name__ == '__main__':
    main()
