import json

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def read_json(fpath):
    """
    Read a JSON file.
    """
    with open(fpath, 'r') as f:
        return json.load(f)


def to_json(data, fpath):
    """
    Save a dict as JSON.
    """
    with open(fpath, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write('\n')


def make_soup(html):
    """
    Make a soup object.

    Examples
    --------
    >>> html = '<html><body><h1>header</h1></body></html>'
    >>> make_soup(html)
    <html><body><h1>header</h1></body></html>

    """
    return BeautifulSoup(html, 'lxml')


def make_headless_chrome():
    """
    Make a headless chrome driver.

    Notes
    -----
    Please download ChromeDriver from the link below if you don't have one.
    https://chromedriver.chromium.org/downloads
    """
    options = Options()
    options.add_argument('--headless')
    user_agent = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.117 Safari/537.36')
    options.add_argument(f'--user-agent={user_agent}')
    return Chrome('./chromedriver', options=options)
