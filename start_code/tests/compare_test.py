import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_8_8_returns_8_is_the_same_as_8(self):
        self.assertEqual("8 is the same as 8", compare(8, 8))

    def test_compare_154_15435_returns_154_is_less_than_15435(self):
        self.assertEqual("154 is less than 15435", compare(154, 15435))
