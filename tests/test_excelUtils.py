# -*- coding: utf-8 -*-

from unittest import TestCase
from .context import excelUtils as uts

class Test(TestCase):
    def test_get_row_number(self):
        self.assertEqual(1, uts.get_row_number('A1'))

    def test_get_column_name(self):
        self.assertEqual('A', uts.get_column_name('A1'))

    def test_split_range_name(self):
        c, r = uts.split_2_number('A1')
        self.assertEqual(0, c)
        self.assertEqual(1, r)
