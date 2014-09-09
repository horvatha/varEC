"""Tests for interval submodule."""

import unittest
from varEC import interval


class TestParseFloatingNumber(unittest.TestCase):

    def test_known_values(self):
        known_values = {
            '200': ("200", None),
            '+200': ("+200", None),
            '200.00': ("200.00", None),
            '20000e-2': ("20000", "-2"),
            '0.0000012': ("0.0000012", None),
            '10': ("10", None),
            '.125': (".125", None),
            '0.125': ("0.125", None),
            '1000': ("1000", None),
            '-2e24': ("-2", "24"),
            '-2e024': ("-2", "024"),
            '6.02e23': ("6.02", "23"),
            '9.81e000': ("9.81", "000"),
        }
        for num_string, result in known_values.items():
            self.assertEqual(interval.parse_floating_number(num_string), result)
            if "e" in num_string:
                self.assertEqual(
                    interval.parse_floating_number(num_string.upper()),
                    result)


class TestNormalizedNumber(unittest.TestCase):

    def test_known_values(self):
        standard = 'standard'
        exponential = 'exponential'
        known_values = {
            '200': (2, 2, standard),
            '200.00': (20000, -2, standard),
            '20000e-2': (20000, -2, exponential),
            '20000e-02': (20000, -2, exponential),
            '0.0000012': (12, -7, standard),
            '10': (1, 1, standard),
            '.125': (125, -3, standard),
            '0.125': (125, -3, standard),
            '1000': (1, 3, standard),
            '-2e24': (-2, 24, exponential),
            '-2e024': (-2, 24, exponential),
            '6.02e23': (602, 21, exponential),
            '9.81e000': (981, -2, exponential),
        }
        for num_string, attributes in known_values.items():
            factor, exponent, format_ = attributes
            normed = interval.NormalizedNumber(num_string)
            self.assertEqual(factor, normed.factor)
            self.assertEqual(exponent, normed.exponent)
            self.assertEqual(format_, normed.format)

    def test_bad_values(self):
        bad_arguments = (
            "001000",
            "-02e3",
            "-02e-33",
            "-02e-33",
        )
        for num_string in bad_arguments:
            with self.assertRaises(ValueError):
                interval.parse_floating_number(num_string)

    def test_convert_to_given_exponent(self):
        known_values = {
            '200': {2: 2, 0: 200, -2: 20000},
            '200.00': {0: 200, -2: 20000},
            '20000e-2': {0: 200, -2: 20000},
            '0.0000012': {-7: 12, -9: 1200},
            '10': {-1: 100, -3: 10000},
            '.125': {-3: 125, -4: 1250},
            '0.125': {-3: 125, -4: 1250},
            '1000': {3: 1, 2: 10, -1: 10000},
            # '-2e24': ,
            # '-2e024': ,
            # '6.02e23': ,
            # '9.81e000': ,
        }
        for num_string in known_values:
            normed = interval.NormalizedNumber(num_string)
            for exponent, factor in known_values[num_string].items():
                normed.convert_to_given_exponent(exponent)
                self.assertEqual(factor, normed.factor)
                self.assertEqual(exponent, normed.exponent)


class TestSameExponent(unittest.TestCase):

    def test_known_values(self):
        known_values = (
            (('-2e23', '3e24'), ([-2, 30], 23, 'exponential')),
            (('1000', '20000'), ([1, 20], 3, 'standard')),
            (('-2', '5'), ([-2, 5], 0, 'standard')),
            (('-2.00', '5'), ([-200, 500], -2, 'standard')),
        )
        for args, result in known_values:
            self.assertEqual(interval.same_exponent(*args), result)


class TestRandom(unittest.TestCase):

    def test_known_values(self):

        known_values = {
            '2.00e16..22e15': (2e16, 22e15),
            '2.00..7': (2, 7),
            '5000..25000': (5000, 25000),
            '10..200': (10, 200),
            '-20..9': (-20, 9),
            '-2.00e-3..9e-3': (-2e-3, 9e-3),
            '-2.00e-7..9e-7': (-2e-7, 9e-7),
            '1,5e3..6,5e3': (1.5e3, 6.5e3),
            '0,1..0,4': (0.1, 0.4),
            '0,12..0,88': (0.12, 0.88),
            '2e-8..16e-8': (2e-8, 16e-8),
            '2E-8..6E-8': (2e-8, 6e-8),
        }
        for i in range(10):
            for interval_, limits in known_values.items():
                min, max = limits
                random_value = interval.random(interval_)
                self.assertGreaterEqual(random_value, min-abs(min)/1000)
                self.assertGreaterEqual(max+abs(max)/1000, random_value)

    def test_small_combinations(self):

        known_values = {
            '2..4': {2, 3, 4},
            '2e16..4e16': {2e16, 3e16, 4e16},
            '2e-16..4e-16': {2e-16, 3e-16, 4e-16},
            '1.9e16..2.2e16': {19e15, 20e15, 21e15, 22e15},
            '19e15..22e15': {19e15, 20e15, 21e15, 22e15},
            '1.97e17..1.99e17': {197e15, 198e15, 199e15},
        }
        for i in range(10):
            for interval_, set_ in known_values.items():
                random_value = interval.random(interval_)
                self.assertIn(random_value, set_)

    # TODO number of significant digits should be checked more cleverly

if __name__ == "__main__":
    unittest.main()
