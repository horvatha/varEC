"""Tests for interval submodule."""

import unittest
from varEC import interval


class TestNormalizedNumber(unittest.TestCase):

    def test_known_values(self):
        standard = 'standard'
        exponential = 'exponential'
        known_values = {
            '200': (2, 2, standard),
            '200.00': (20000, -2, standard),
            '20000e-2': (20000, -2, exponential),
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


if __name__ == "__main__":
    unittest.main()
