from datetime import date
from unittest import TestCase

from projeto2.actions import str_to_date


class StringToDate(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str_to_date(self):
        result = str_to_date('2019-12-24')
        self.assertEqual(result, date(year=2019, month=12, day=24))
        self.assertEqual(type(result), type(date(year=2019, month=12, day=24)))
        self.assertEqual(type(result), date)

    def test_return_2019_01_01(self):
        pass

    def test_return_invalid_date(self):
        self.assertRaises(ValueError, lambda: str_to_date('2019-13-01'))
