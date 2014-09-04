"""Tests for possibilities module."""

from __future__ import print_function
import unittest
from varEC import gadgets


class TestGetDate(unittest.TestCase):
    """Test date_string() function"""

    def setUp(self):
        self.known_values = (
            ('140923', '2014. szeptember 23.'),
            ('140923almafa', '2014. szeptember 23.'),
            ('140101almafa', '2014. január 1.'),
            ('410101matematika_pot_zh', '2041. január 1.'),
        )

    def test_known_values(self):
        for file_name, date_string in self.known_values:
            self.assertEqual(gadgets.date_string(file_name), date_string)

    def test_bad_values(self):
        for file_name in "141302 alma140211 141132 141131".split():
            with self.assertRaises(AssertionError):
                gadgets.date_string(file_name)


class TestTomorrowTriple(unittest.TestCase):
    """Test tomorrow_triple() function"""

    def test_can_be_good(self):
        date = year, month, day = gadgets.tomorrow_triple()
        self.assertGreater(year, 2013)
        self.assertTrue(0 < month < 13)
        self.assertTrue(0 < day < 32)
        for i in date:
            self.assertIsInstance(i, int)


class TestTextIn(unittest.TestCase):
    """Test textin() function"""

    def test_bad_values(self):
        for args, kwargs in (
            (("samu", "Testpaper"), {}),  # bad type_
            (("samu",), {"type_": "Testpaper"}),  # bad type_
        ):
            with self.assertRaises(AssertionError):
                gadgets.textin(*args, **kwargs)


class TestTable(unittest.TestCase):
    """Test table() function"""

    def test_bad_values(self):
        points = (40, 12, 13, 14, 56)
        text = r"""\begin{tabular}[b]{|r|r|r|r|r|r|}
\hline
1.&	2.&	3.&	4.&	5.&	Össz.\\
\hline
&	&	&	&	&	\\
\hline
40&	12&	13&	14&	56&	135\\
\hline
\end{tabular}
"""
        self.assertEqual(gadgets.table(*points), text)


if __name__ == "__main__":
    unittest.main()
