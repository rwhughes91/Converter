import unittest

from Converter import Converter


class TestConstruction(unittest.TestCase):

    def test_empty_false(self):
        with self.assertRaises(TypeError):
            s = Converter()

    def test_con_pos(self):
        s = Converter(2017, "CHF")


class TestAttributes(unittest.TestCase):

    def setUp(self):
        self.s = Converter(2017, "CHF")

    def test_year_pos(self):
        self.assertTrue(self.s.year == 2017)

    def test_year_false(self):
        self.assertFalse(self.s.year == 2018)

    def test_orig_curr_pos(self):
        self.assertTrue(self.s.orig_curr == "CHF")

    def test_orig_curr_neg(self):
        self.assertFalse(self.s.orig_curr != "CHF")

    def test_types_pos(self):
        self.assertTrue(type(self.s.year) == int and type(self.s.orig_curr) == str)


class TestDateGen(unittest.TestCase):

    def setUp(self):
        self.s = Converter(2017, "USD")
        self.s.date_gen()

    def test_date_gen_pos(self):
        self.assertTrue(self.s.date_spread)

    def test_date_gen_neg(self):
        self.assertFalse(self.s.date_spread == [])

    def test_date_gen_length_outer(self):
        self.assertTrue(len(self.s.date_spread) == 12)
        self.assertFalse(len(self.s.date_spread) != 12)

    def test_date_gen_length_inner(self):
        self.assertFalse(len(self.s.date_spread[11]) == 1)
        self.assertTrue(len(self.s.date_spread[11]) == 31)

