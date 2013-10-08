#!/usr/bin/env python
# coding: utf-8

"""New module to create variations for an example.
"""

from __future__ import division
from __future__ import print_function

import itertools
import re

__author__ = 'Arpad Horvath'

# Used in unittest.
def varsets_from_string(eqs):
    return tuple([frozenset(eq.split()) for eq in eqs.split(',')])

def get_variables(formula):
    "Returns with the variables in the formula."

    var_pattern = re.compile('''
        (
       [a-zA-Z] # first character is letter
       \w*      # alphanumeric characters
       )
       (
         [^(\w]   # not opening bracket at the end (not a function)
           |
         $        # it can be at the end of the string
       )
       ''', re.VERBOSE)

    vars = formula[:]
    variables = set()
    scan_from = 0
    while True:
        remainder = vars[scan_from:]
        var1 = var_pattern.search(vars[scan_from:])
        if var1:
            var = var1.group(1)
            start, end = var1.span()
            if var in set('eE') and start != 0 and remainder[start-1] in set('.0123456789'):
                pass
            elif var not in variables:
                variables.add(var1.group(1))
            scan_from += end
        else:
            break
    return variables

def make_equations(formulas, variables):
    """docstring for make_equations"""
    equations = []
    for formula in formulas:
        variables_in_formula = get_variables(formula) & variables
        equations.append(variables_in_formula)
    return tuple(equations)

def possibilities(equations, protected_variables=None):
    vars = set()
    if protected_variables is None:
        protected_variables = frozenset()
    for eq in equations:
        vars |= eq
    vars = sorted(vars)
    possibilities = []
    number_of_free_variables = len(vars)-len(equations)
    assert len(protected_variables) <= number_of_free_variables, 'too many protected variables'
    for initial in itertools.combinations(vars, number_of_free_variables):
        initial = frozenset(initial)
        if protected_variables <= initial and len(calculatable(initial, equations, vars)) == len(vars):
            possibilities.append(initial)
    return possibilities

def calculatable(initial, equations, vars):
    if isinstance(initial, str):
        initial = initial.split()
    assert len(vars) - len(equations) == len(initial), 'wrong number of values in initial'
    calculatable = set(initial)
    new_calc = True  # Just to enter the cycle
    while new_calc:
        new_calc = new_calculatable(calculatable, equations)
        calculatable |= new_calc
    return calculatable

def new_calculatable(calculatable, equations):
    """docstring for new_calculatable"""
    new_calculatable = set()
    for eq in equations:
        diff = eq - calculatable
        if len(diff) == 1:
            new_calculatable |= diff
    return new_calculatable

