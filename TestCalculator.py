from unittest import TestCase

from Calculator import Calculator

class TestCalculator(TestCase):
    def test_sum(self):
        self.assertEqual(Calculator().sum(""), 0, "Empty string")