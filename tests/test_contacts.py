import unittest
import sys

try:
    from contacts import *
except ImportError as e:
    # ImportError when ran as a script. Hence append the path for correct imports
    from os.path import dirname, join
    PROJECT_PATH = dirname(dirname(__file__))
    sys.path.append(join(PROJECT_PATH, "contacts"))
    from contacts import *


class ValidNamesTest(unittest.TestCase):

    def test_is_valid_name(self):
        self.assertTrue(is_valid_name("Chris Cummins"))
        self.assertTrue(is_valid_name("Chris"))
        self.assertFalse(is_valid_name("Chris "))
        self.assertFalse(is_valid_name("Chris123"))
        self.assertFalse(is_valid_name("123Chris"))
        self.assertFalse(is_valid_name("Chris Catherine "))
        self.assertFalse(is_valid_name(" Chris Catherine"))


class StoreNamesTest(unittest.TestCase):

    def setUp(self):
        self.names = []

    @classmethod
    def tearDownClass(cls):
        pass

    def test_contact_store(self):
        self.assertEqual(store_contact("Chris Catherine", self.names), ["Chris Catherine"])
        self.assertEqual(store_contact("Chris Donald", self.names), ["Chris Catherine", "Chris Donald"])


class SearchNamesTest(unittest.TestCase):

    def setUp(self):
        self.names = ['Chris Andrews', 'Chan Hang', 'Harris Cale', 'Name Chris', 'Christopher Nolan']

    @classmethod
    def tearDownClass(cls):
        pass

    def test_search_contact(self):
        names = self.names
        self.assertEqual(search_contact("Chris", names), ['Chris Andrews', 'Name Chris', 'Christopher Nolan'])
        self.assertEqual(search_contact("Ch", names), ['Chris Andrews', 'Chan Hang', 'Christopher Nolan', 'Name Chris'])
        self.assertEqual(search_contact("DoesNotExist", names), [])

if __name__ == "__main__":
    unittest.main()
