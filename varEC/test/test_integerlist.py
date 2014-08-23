"""Test for integerlist.py"""
import unittest
from varEC import integerlist


class TestIntegerList(unittest.TestCase):
    """TestGroup"""

    def setUp(self):
        """Setup Tests"""
        self.known_values = (
            ([5, 7, 2, 4, 3, 9, 8, 8, 1, 10, 7, 7, 2, 2,
              50, 50, 51, 25, 101, -2, -3, -4],
             [(-4, -2), (1, 5), (7, 10), (25, 25), (50, 51), (101, 101)],
             "-4..-4 1..1 7..7 25 50..50 101"),
        )
        self.mixed_lists = (
            [1.0, 5.0],
            [1, 5.3, "a"],
            [1, 5, "a"],
            [1, None, 3],
        )

    def test_integerlist_raises_if_mixed_list(self):
        for mixed_list in self.mixed_lists:
            with self.assertRaises(AssertionError):
                integerlist.IntegerList(mixed_list)

    def test_make_intervals_return_proper_value(self):
        for list_of_integers, result, _ in self.known_values:
            list_of_integers = integerlist.IntegerList(list_of_integers)
            self.assertEqual(list_of_integers.intervals, result)

    def test_str_return_proper_value(self):
        for list_of_integers, _, string in self.known_values:
            list_of_integers = integerlist.IntegerList(list_of_integers)
            self.assertEqual(str(list_of_integers), string)


class TestUnique(unittest.TestCase):

    def setUp(self):
        """Setup Tests"""
        self.known_values = (
            ([-1, -1, 1, 1, 4, 3, 3, 3,
              None, None, None, None, None, None, None, None, None],
             {1: 2, -1: 2, 3: 3, None: 9}),
            ([1, 1, 1, 1, 1, 2, 3, 3, 3, 5, "a", "a",
              9, 9, 9, 9, 9, 9, 9, 9],
             {1: 5, 3: 3, 'a': 2, 9: 8}),
        )

    def test_str_return_proper_value(self):
        for list_, result in self.known_values:
            self.assertEqual(integerlist.search_not_uniq(list_), result)


if __name__ == "__main__":
    unittest.main()
