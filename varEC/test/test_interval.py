"""Tests for interval submodule."""

import unittest
from varEC import interval


class TestExponent(unittest.TestCase):

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
            a = interval.Exponential(num_string)
            self.assertEqual(factor, a.factor)
            self.assertEqual(exponent, a.exponent)
            self.assertEqual(format_, a.format)


class TestSameExponent(unittest.TestCase):

    def test_known_values(self):
        known_values = (
            (('-2e23', '3e24'), ([-2, 30], 23, None, 'exponential')),
            (('1000', '20000'), ([1, 20], 3, None, 'standard')),
            (('-2', '5'), ([-2, 5], 0, None, 'standard')),
            (('-2.00', '5'), ([-200, 500], -2, None, 'standard')),
        )
        for args, result in known_values:
            self.assertEqual(interval.same_exponent(*args), result)


if __name__ == "__main__":
    unittest.main()
