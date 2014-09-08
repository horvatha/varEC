#!/usr/bin/env python3

r""" The main function is random(interval):
  random(interval) --> value

  interval:  for example    12..88  or 7e10..2e11
  value:  a value in the interval
  latex:  the latex form of the value

  See: https://github.com/horvatha/varEC/
"""

from __future__ import print_function

from random import randint


class Exponential:
    def __init__(self, num_string):
        self.factor = None
        self.exponent = None
        self.format = 'standard'
        self.dec_point = None
        self.set(num_string)

    def set(self, num_string):
        """set(self, num_string) --> None

        Sets the variables below.

        e.g. set('-1,5e23')  -->
             self.factor = -15,
             self.exponent = 22,
             self.format = 'exponential'
                  (It is 'standard', if there is not an 'e' in num_string.)
             self.dec_point = ','  # In Hungary the decimal 'point' is ','
        """
        num_string = num_string.strip()  # ' -03.23e015  ' --> '-03.23e015'

        if ',' in num_string:
            dec_point = ','
            num_string = num_string.replace(',', '.')
        if '.' in num_string:
            dec_point = '.'
        else:
            dec_point = None

        # Sign
        if num_string[0] == '-':
            sign = -1
            num_string = num_string[1:]   # '03.23e015'
        elif num_string[0] == '+':
            sign = +1
            num_string = num_string[1:]
        else:
            sign = +1  # Unfortunately it is +1 too, if the value is 0.

        # Delete the zeros at the beginning of num_string.
        while num_string[0] == '0' and len(num_string) > 1:   # '3.23e015'
            num_string = num_string[1:]
            # num_string.pop(0)  # Doesn't work it in python2.0. In 1.5 not.

        # One character number
        if len(num_string) == 1:
            self.factor = sign*int(num_string)
            self.exponent = 0
            return

        #  Handling of 'e'
        num_string.lower()  # 'E' --> 'e' if it is any
        parts = num_string.split('e')  # ('3.23', '15')
        if len(parts) == 1:
            self.format = 'standard'
            self.exponent = '0'  # Exponent is 0.
            self.factor = parts[0]
        elif len(parts) == 2:
            self.factor, self.exponent = parts
            self.format = 'exponential'
        else:
            raise ValueError("more then one 'e' is in the number_string")
        self.exponent = int(self.exponent)

        # Handling of dec_point '.'
        factor_parts = self.factor.split('.')
        if len(factor_parts) == 2:  # There is a point in it.
            integer, fract = factor_parts
            self.exponent = self.exponent - len(fract)
            self.factor = integer + fract     # ('323', 13)

        # Delete the zeros at the beginning of factor.
        while self.factor[0] == '0':
            self.factor = self.factor[1:]

        # It handels the zeros at the end of the factor
        # if it is an integer.
        if self.exponent >= 0:
            while self.factor[-1] == '0':
                self.factor = self.factor[:-1]
                self.exponent = self.exponent + 1

        self.factor = sign * int(self.factor)      # (-323, 13)

    def __str__(self):
        return "Exponential(%de%d, %s)" % (
            self.factor, self.exponent, self.format
        )


def same_exponent(num_string1, num_string2):
    """same_exponent(num_string1, num_string2) -->
           [factor1, factor2], common_exponent, dec_point, format

    It writes the the given numbers into
                          a "factor * 10**common_exponent" format.

    num_string1, num_string2: two number in string format
    factor1, factor2: the factor of the first and second number
    dec_point can be '.' or ','
    format can be 'standard or 'exponential' """

    exp1 = Exponential(num_string1)
    exp2 = Exponential(num_string2)
    common_exponent = min(exp1.exponent, exp2.exponent)

    for exp in [exp1, exp2]:
        diff = exp.exponent - common_exponent
        if diff:
            exp.exponent = exp.exponent - diff
            exp.factor = exp.factor * (10**diff)

    if exp1.factor > exp2.factor:
        raise ValueError('the first number in the interval is the bigger')

    # format
    if exp1.format == exp2.format == 'standard':
        format = 'standard'
    else:
        format = 'exponential'

    return [exp1.factor, exp2.factor], common_exponent, format


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
#   if len(`value`) > 1:
#     delta = len(`value`) - 1
#     newexponent = exponent - delta
#     value = float(value) / (10.0)
    value = newfactor*10.0**exponent
    return value


def random_test():
    for intv in ['2.00e16..22e15', '2.00..7', '5000..25000',
                 '10..200', '-20..9', '-2.00e-3..9e-3', '-2.00e-7..9e-7',
                 '1,5e3..6,5e3', '0,1..0,4', '0,12..0,88',
                 '2e-8..16e-8', '2E-8..6E-8']:
        print('\n****', intv)
        for i in range(3):
            print('In interval %s is %s. (LaTeX form: %s)' %
                  (intv, random(intv)))


if __name__ == '__main__':
    random_test()
