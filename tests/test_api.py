import api
import unittest
import sys
# This is so janky omg
sys.path.append(sys.path[0].split('/test')[0])

# These tests need to be properly implemented


class TestAPI(unittest.TestCase):

    def test_get_user(self):
        user = api.get_user('jawkneelin')
        self.assertIsNotNone(user)

    def test_get_bio(self):
        user = api.get_user('jawkneelin')
        self.assertIsNotNone(user.get_bio())

    def test_get_num_followed(self):
        user = api.get_user('jawkneelin')
        self.assertIsNotNone(user.get_num_followed())

    def test_get_num_followers(self):
        user = api.get_user('jawkneelin')
        self.assertIsNotNone(user.get_num_followers())


if __name__ == '__main__':
    unittest.main()
