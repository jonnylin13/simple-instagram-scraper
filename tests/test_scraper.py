from bs4 import BeautifulSoup
import scraper
import unittest
import sys
# This is so janky omg
sys.path.append(sys.path[0].split('/test')[0])


class TestScraper(unittest.TestCase):

    def test_get_file_by_url(self):
        scraped = scraper.get_file_by_url('https://instagram.com/jawkneelin')
        self.assertEqual(scraped, '.scraped/jawkneelin')

    def test_fetch(self):
        soup = scraper.fetch('https://instagram.com/jawkneelin', False)
        self.assertEqual(type(soup), BeautifulSoup)


if __name__ == '__main__':
    unittest.main()
