from bs4 import BeautifulSoup
import urllib.request
import os
import re
import json

SCRAPED_DIR = '.scraped/'

# Returns the filepath from instagram URL


def get_file_by_url(url):
    username = url.split('/')[-1]
    return os.path.join(SCRAPED_DIR, username)

# Fetches the soup


def fetch(url, load):
    filepath = get_file_by_url(url)
    if os.path.isfile(filepath) and load:
        # Load the saved one instead
        loaded = open(filepath, 'r')
        soup = BeautifulSoup(loaded, 'html.parser')
        loaded.close()
        return soup
    else:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        save(url, soup)
        return soup

# Saves the soup into a file


def save(url, soup):
    if not os.path.exists('.scraped'):
        print('Creating .scraped/ directory.')
        os.mkdir('./{}'.format(SCRAPED_DIR))
    try:
        file = open(get_file_by_url(url), 'w')
        file.write(str(soup))
        file.close()
        print('Saved scrape file: {}'.format(url))
    except Exception as e:
        print('Something went wrong saving file: {}'.format(url))
        print(e)

# Takes soup object, returns the sharedData using regex


def _get_data(soup):
    result = re.search(r"_sharedData = (.*)</script", str(soup))
    if result is None:
        print('Could not find sharedData.')
    return result.group(1).split(';')[0]

# Convenience function


def get_data(url, load=True):
    raw = _get_data(fetch(url, load))
    # This function will error out
    # unlike the unsafe one above
    data = (json.loads(str(raw)))
    return data
