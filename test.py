import unittest
from main import *

class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2, 2), 4)

if __name__ == "__test__":
    unittest.test()
