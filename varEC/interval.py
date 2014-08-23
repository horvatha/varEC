#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  -*- Python -*-

r""" The main function is random(interval):
  random(interval) --> value, latex

  interval:  for example    12..88  or 7e10..2e11
  value:  a value in the interval
  latex:  the latex form of the value

  See: www.roik.bmf.hu/~ahorvath/feladatsor
   (It's only in Hungarian language this time.) """
from __future__ import print_function


old_docstring=r"""
 Functions:
   one_testpaper
     uses: random
             uses: same_exponent
             uses: set in class Exponential
     uses: test_text in class IntervalList
             uses: getintervals in class IntervalList
                     uses:  add_interval in class IntervalList

 Number formats:
  exponential -- there's 'e' in it. (1.2e24)
  standard --    others   (234.24 or 144)

 Variables:
   num_string:   The string format of the number.
                 This format is same as it is in Python.
   factor and exponent: the number is factor * (10 ** exponent)
         factor is always integer
   value: the value of the number
   format: see 'Number formats'

   vstring: the latex format of the number
   dec_point: the decimal point, '.' or ','
   times:  the multiplication sign in latex
       usually  \times or \cdot


 """

##################################################
## import part
##################################################
import os
from random import randint, choice
import re
#import re

from .lang import lang

try:
  exec('from .setup_%s import decimal_point, times' % lang)
except ImportError:
  print("I use english instead of %s." % lang)
  from .setup_en import decimal_point, times


try:
  exec('from .lang_%s import env, mesg, err' % lang)
except ImportError:
  print("I use english instead of %s." % lang)
  from .lang_en import env, mesg, err

verbose = 0

## if lang in ['hu']:
##   times = r"\cdot"
## elif lang in ['en', 'us']:
##   times = r"\times"
## else:
##   print("There is no support for language %s according to multiplication sign." % lang)
##   times = r"\times"

###############################################
##
## Part 1.  Make a random number in an interval
##
###############################################

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
         self.format = 'exponential'    (It is 'standard', if there is not an 'e' in num_string.)
         self.dec_point = ','  # In Hungary the decimal 'point' is ',', not '.'
    """
    num_string = num_string.strip()  # ' -03.23e015  ' --> '-03.23e015'

    if ',' in  num_string:
      dec_point = ','
      num_string = num_string.replace(',', '.')
    if '.' in  num_string:
      dec_point = '.'
    else:
      dec_point = None

    # Sign
    if  num_string[0] == '-':
      sign = -1
      num_string = num_string[1:]   # '03.23e015'
    elif  num_string[0] == '+':
      sign = +1
      num_string = num_string[1:]
    else: sign = +1  # Unfortunately it is +1 too, if the value is 0.

    # Delete the zeros at the beginning of num_string.
    while num_string[0] == '0' and len(num_string) > 1:   # '3.23e015'
      num_string = num_string[1:]
      #num_string.pop(0)  # Doesn't work it in python2.0. In 1.5 not.

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
    factor_parts =  self.factor.split('.')
    if len(factor_parts) == 2: # There is a point in it.
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

##   # Makes two (valuable??) digits if it is less
##   #hu legalább két értékes jegy
##   if len(factor) == 1:
##     factor = factor + '0'
##     exponent = exponent - 1

    self.factor = sign * int(self.factor)      # (-323, 13)

  def __str__(self):
    try:
        string = "%de%d (%s)" % (self.factor, self.exponent, self.format)
    except TypeError:
        string = 'Not well defined.'
    return string


def Exponent_test():
  a = Exponential()
  for num_string in ['200','10','1000','-2e24']:
    a.set(num_string)
    print(num_string, a)
    print('Factor: %d, exponent: %d, format: %s' % (a.factor, a.exponent, a.format))


## It was the original plan
##############################

##   """ good_exponent(num_string) --> (factor, exponent)

##    e.g.  if num_string is '-03.23e015' it gives (-323, 13)
##    (The spaces around it are allowed, but in it no.
##     good: ' 15' , bad: '3 e5')

##    1. The factor is the integer. (The smallest with?? the contitions 1-3)
##    2. If there are some zeros after the '.' it will be included in factor.
##        '1.00' --> (100, -2)

##    3. If it is an integer (whithout '.' and 'e') the exponent will be
##      not negativ.  (If it is 'integer' then the output is 'integer'.)
##        '1' --> (1, 0)

##    The 4. point is only a plan.
## ##    4. If there is no stronger condition, the output has 2 significant digits.
## ##   """


def same_exponent(num_string1, num_string2):
  """same_exponent(num_string1, num_string2) --> [factor1, factor2], common_exponent, dec_point, format

  It writes the the given numbers into a "factor * 10**common_exponent" format.

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

  ## decimal point (usually '.' or ',')
  if exp1.dec_point == None:
    exp1.dec_point = exp2.dec_point
  elif exp2.dec_point == None:
    exp2.dec_point = exp1.dec_point

  if exp1.dec_point == exp2.dec_point:
    dec_point = exp1.dec_point
  else:
    raise ValueError('there are two types of decimal point')

  return [exp1.factor, exp2.factor], common_exponent, dec_point, format

def same_exponent_test():
  #same_exponent = same_exponent2
  print("same_exponent( '-2e23','3e24' )    -->",)
  print(same_exponent( '-2e23','3e24' ))

  print("same_exponent( '1000','20000' )    -->",)
  print(same_exponent( '1000','20000' ))

  print("same_exponent( '-2','5' )    -->",)
  print(same_exponent( '-2','5' ))

  print("same_exponent( '-2.00','5' )    -->",)
  print(same_exponent( '-2.00','5' ))

def random(interval, verbose = 0):
  """ random(interval) --> value, latex

 value is a random number in the interval. The latex is the latex form of value.
 The value is in an integer form, if it is possible."""

  if verbose > 0: print("** interval.random() running")
  if verbose > 1: print(' Interval: %s' % interval)
  num_string1, num_string2 = interval.split('..')
  num_string1 = num_string1.replace('E', 'e')
  num_string2 = num_string2.replace('E', 'e')
  factors, exponent, dec_point2, format = same_exponent(num_string1, num_string2)

  factor1, factor2 = factors
  if factor1 != 0:
    ratio = abs(factor2/factor1)
  else: ratio = 100000
# It could be logaritmical ... if ratio >10
  if ratio >= 500:
    raise ValueError('too much range')


  newfactor = randint(factor1, factor2)
##   if len(`value`) > 1:
##     delta = len(`value`) - 1
##     newexponent = exponent - delta
##     value = float(value) / (10.0)
  value = newfactor*10.0**exponent


  latex = value2latex(value)
  return value, latex


def value2latex(value, verbose=0):
  """ It converts a value to LaTeX format."""

##   try:
##     if value == int(value):
##       if verbose: print('interval.value2latex(): integer')
##       return str(int(value))
##   except OverflowError:
##     pass

  #vstring = '%.4g' % value
  vstring = '%.8g' % value
  if 'e' in vstring:
    vstring = vstring.replace('e', times + '10^{') + '}'
  if '.' in vstring and decimal_point != '.':
    vstring = vstring.replace('.', decimal_point)

  latex = vstring.replace('+', '')
  return latex

def random_test():
  for intv in ['2.00e16..22e15', '2.00..7', '5000..25000','10..200','-20..9','-2.00e-3..9e-3', '-2.00e-7..9e-7', '1,5e3..6,5e3', '0,1..0,4', '0,12..0,88', '2e-8..16e-8', '2E-8..6E-8']:
    print('\n****', intv)
    for i in range(3):
      num, string = random(intv)
      print('In interval %s is %s. (LaTeX form: %s)'  % (intv, str(num), string))

##   print
##   for i in range(20):
##     print(random('0..1'),)

##   list = [0]*10
##   for i in range(1000):
##     num = random('1..9')
##     list[num] = list[num] + 1
##   list.sort()
##   print(list)


########################################
##
##   Part 2:   Test
##
########################################

def test():
  "Uncomment the item you want to test."
  #test1()
  #same_exponent_test()
  random_test()
  #Exponent_test()
  #Variation_test()

if __name__ == '__main__':
  test()
