from unittest import TestCase

from Calculator import Calculator

class TestCalculator(TestCase):
    def test_sum(self):
        self.assertEqual(Calculator().sum(""), 0, "Empty string")

    def test_sum_string(self):
        self.assertEqual(Calculator().sum("1"), 1, "A number")

    def test_sum_string_with_num(self):
        self.assertEqual(Calculator().sum("1"), 1, "A number")
        self.assertEqual(Calculator().sum("2"), 2, "A number")

    def test_sum_string_with_two_nums(self):
        self.assertEqual(Calculator().sum("1,3"), 4, "Two numbers")