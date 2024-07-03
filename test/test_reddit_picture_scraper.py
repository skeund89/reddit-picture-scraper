import unittest
from scraper import pictureScraper

class TestPictureScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = pictureScraper()

    def test_read_file(self):
        links = self.scraper.read_file('test/subreddit_links.txt')
        self.assertEqual(links, ['https://old.reddit.com/r/pics/', 'https://old.reddit.com/r/aww/'])

    def test_fetch_imagelinks(self):
        links = self.scraper.fetch_imagelinks('Safari', None, 'https://old.reddit.com/r/aww/', 100)
        self.assertTrue(len(links) > 0)

if __name__ == '__main__':
    unittest.main()