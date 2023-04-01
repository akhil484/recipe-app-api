"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """Test adding numbers together"""

        res = calc.add(5, 7)

        self.assertEqual(res,12)

    def test_subtract_numbers(self):
        """Subtracting Numbers"""

        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
        