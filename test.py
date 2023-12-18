# File: test_atg_world.py

import unittest
import requests

class TestAtgWorldWebsite(unittest.TestCase):
    def test_website_accessibility(self):
        url = "https://atg.world"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Failed to access {url}")

if __name__ == '__main__':
    unittest.main()
