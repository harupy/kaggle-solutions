import json
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def read_json(fpath):
    """
    Read a JSON file.

    Examples
    --------
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     data = {'a': 0}
    ...     fpath = os.path.join(tmpdir, 'data.json')
    ...     with open(fpath, 'w') as f:
    ...         json.dump(data, f)
    ...     data == read_json(fpath)
    True

    """
    with open(fpath, 'r') as f:
        return json.load(f)


def to_json(data, fpath):
    """
    Save a dict as JSON.

    Examples
    --------
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     data = {'a': 0}
    ...     fpath = os.path.join(tmpdir, 'data.json')
    ...     to_json(data, fpath)
    ...     os.path.exists(fpath)
    True

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
    """
    options = Options()
    options.add_argument('--headless')
    return Chrome('./chromedriver', options=options)
