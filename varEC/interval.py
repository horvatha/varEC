#!/usr/bin/env python3

r""" The main function is random(interval):
  random(interval) --> value

  interval:  for example    12..88  or 7e10..2e11
  value:  a value in the interval

  See: https://github.com/horvatha/varEC/
"""

from __future__ import print_function

from random import randint
import re


def parse_floating_number(num_string):
    floating_point_regexp = re.compile(
        """
        (?P<significand>
           [+-]?
           (
           ([1-9][0-9]*\.?[0-9]*)
           |
           (0?\.[0-9]+)
           )
        )
        ([Ee](?P<exponent>[+-]?[0-9]+))?
        """,
        re.VERBOSE
    )
    match = floating_point_regexp.match(num_string)
    if match is None:
        raise ValueError("It is not a well-formed floating point number.")
    groupdict = match.groupdict()
    list_ = [groupdict.get(key, None)
             for key in "significand exponent".split()]
    return tuple(list_)


def is_one_digit(num_string):
    if num_string[0] in "+-":
        num_string = num_string[1:]
    return len(num_string) == 1


class NormalizedNumber:
    def __init__(self, num_string):
        self.factor = None
        self.exponent = None
        self.format = 'standard'
        self.set(num_string)

    def set(self, num_string):
        """set(self, num_string) --> None

        Sets the variables below.

        e.g. set('-1,5e23')  -->
             self.factor = -15,
             self.exponent = 22,
             self.format = 'exponential'
                  (It is 'standard', if there is not an 'e' in num_string.)
        """
        num_string = num_string.strip().lower()
        # ' -03.23E015  ' --> '-03.23e015'
        num_string = num_string.replace(',', '.')
        factor, exponent = \
            parse_floating_number(num_string)

        if exponent is None and is_one_digit(factor):
            self.factor = int(factor)
            self.exponent = 0
            return

        if exponent is None:
            self.format = 'standard'
            self.exponent = '0'
            self.factor = factor
        else:
            self.factor, self.exponent = factor, exponent
            self.format = 'exponential'
        self.exponent = int(self.exponent)

        # Handling of dec_point '.'
        factor_parts = self.factor.split('.')
        if len(factor_parts) == 2:  # There is a point in it.
            integer, fract = factor_parts
            self.exponent = self.exponent - len(fract)
            self.factor = integer + fract     # ('323', 13)

        # It handels the zeros at the end of the factor
        # if it is an integer.
        if self.exponent >= 0:
            while self.factor[-1] == '0':
                self.factor = self.factor[:-1]
                self.exponent = self.exponent + 1

        self.factor = int(self.factor)      # (-323, 13)

    def convert_to_given_exponent(self, exponent):
        assert isinstance(exponent, int)
        exponent_diff = self.exponent - exponent
        if not exponent_diff:
            return
        self.exponent = exponent
        self.factor = self.factor * 10**exponent_diff

    def __str__(self):
        return "NormalizedNumber(%de%d, %s)" % (
            self.factor, self.exponent, self.format
        )


def same_exponent(num_string1, num_string2):
    """same_exponent(num_string1, num_string2) -->
           [factor1, factor2], common_exponent, format

    It writes the the given numbers into
                          a "factor * 10**common_exponent" format.

    num_string1, num_string2: two number in string format
    factor1, factor2: the factor of the first and second number
    format can be 'standard or 'exponential' """

    normalized_number1 = NormalizedNumber(num_string1)
    normalized_number2 = NormalizedNumber(num_string2)
    common_exponent = min(normalized_number1.exponent,
                          normalized_number2.exponent)

    for normalized_number in [normalized_number1, normalized_number2]:
        normalized_number.convert_to_given_exponent(common_exponent)

    if normalized_number1.factor > normalized_number2.factor:
        raise ValueError('the first number in the interval is the bigger')

    if normalized_number1.format == normalized_number2.format == 'standard':
        format = 'standard'
    else:
        format = 'exponential'

    return [normalized_number1.factor,
            normalized_number2.factor], common_exponent, format


def random(interval):
    """ random(interval) --> value

   value is a random number in the interval.
   The value is in an integer form, if it is possible."""

    num_string1, num_string2 = interval.split('..')
    num_string1 = num_string1.replace('E', 'e')
    num_string2 = num_string2.replace('E', 'e')
    factors, exponent, format = \
        same_exponent(num_string1, num_string2)

    factor1, factor2 = factors
    if factor1 != 0:
        ratio = abs(factor2/factor1)
    else:
        ratio = 100000
    # TODO It could be logaritmical ... if ratio >10
    if ratio >= 500:
        raise ValueError('too much range')

    newfactor = randint(factor1, factor2)
    value = newfactor*10.0**exponent
    return value
