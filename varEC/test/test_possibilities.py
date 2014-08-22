"""Tests for possibilities module."""

from __future__ import print_function
import unittest
from varEC import possibilities
varsets_from_string = possibilities.varsets_from_string


class TestGetVariables(unittest.TestCase):
    """Test get_variables() function"""

    formulas = (
        ('s=v*t', 's v t'),
        ('Em=0.5*m*v**2', 'Em m v'),
        ('Eh=m*9.81*h*2e-16', 'Eh m h'),
        ('k=e+s+s**2', 'k e s'),
        ('r=100*sqrt(2*E*9.11e-31)/(qe*6e-5)', 'r qe E'),
        ('E=Ev*qe', 'E Ev qe'),
        ('v=sqrt(2*E/9.11e-31)', 'v E'),
        ('v=sqrt(2*Em/9.11E-31)', 'v Em'),
        ('v=sqrt(2*Em/9.E-31)', 'v Em'),
        ('v_r=sqrt(2*E_m/9.E-31*potential_energy)', 'v_r E_m potential_energy'),
    )

    def test_known_values(self):
        "get_variables() should return proper values"
        for formula, known_variables in self.formulas:
            known_variables = set(known_variables.split())
            variables = possibilities.get_variables(formula)
            self.assertEqual(variables, known_variables)


class TestHelperFunctions(unittest.TestCase):
    """Test helper functions"""

    varsets_from_string = (
        ('t,d v0 t,v v0 t,alpha v0 v,E v',
         (frozenset('t'), frozenset(['d', 'v0', 't']),
          frozenset(['v', 'v0', 't']), frozenset(['alpha', 'v0', 'v']),
          frozenset(['E', 'v']))),
        ('t, d v0 t, v v0 t , alpha v0 v , E v',
         (frozenset('t'), frozenset(['d', 'v0', 't']),
          frozenset(['v', 'v0', 't']), frozenset(['alpha', 'v0', 'v']),
          frozenset(['E', 'v']))),
        ('d v0 t', (frozenset(['d', 'v0', 't']),)),
    )

    def test_varsets_from_string(self):
        "varsets_from_string() should return proper values"
        for string, known_equations in self.varsets_from_string:
            self.assertEqual(varsets_from_string(string), known_equations)


class TestMakeEquations(unittest.TestCase):
    """Test make_equations() function"""

    formulas = (
        (['t=sqrt(2*125/g)', 'd=v0*t', 'v=sqrt(v0**2+(g*t)**2)',
          'alpha=acos(v0/v)*180/pi', 'E=v*v'],
            set('v0 t d v alpha E'.split()),
            varsets_from_string('t,d v0 t,v v0 t,alpha v0 v,E v')),
        (['h=g/2*t*t', 'd=v0*t', 'v=sqrt(v0**2+(g*t)**2)',
          'alpha=acos(v0/v)*180/pi', 'Em=0.5*m*v*v'],
            set('m v0 h t v d alpha Em'.split()),
            varsets_from_string('h t,d v0 t,v v0 t,alpha v0 v,Em m v')),
    )

    def test_known_values(self):
        "get_variables() should return proper values"
        for formulas, variables, known_equations in self.formulas:
            self.assertEqual(possibilities.make_equations(formulas, variables),
                             known_equations)


class TestPossibilities(unittest.TestCase):
    """Test possibilities function and its helper functions."""

    def setUp(self):
        """Setup Tests"""
        raw_values = {
            'a b c,b c d,a b e,c f,d f g':
            (
                'b e,a,c,d f,g',
                'b f,c,d a,e g',
                'b g',
                'c g,f,d,b,a,e',
                'e g',
            )
        }
        self.known_values = {
            varsets_from_string(key):
            [[set(vars.strip().split()) for vars in calc_parts.split(',')]
             for calc_parts in raw_values[key]]
            for key in raw_values
        }
        self.possibilities = {
            varsets_from_string('a b c,b c d,a b e,c f,d f g'):
            varsets_from_string('a b,a c,a e,a f,c b,b d,b e,'
                                'b f,c d,c g,d f,d g,g f'),
            varsets_from_string('t h,t v v0,Em m v,alpha v0 v'):
            varsets_from_string('m v alpha,h v m,Em alpha v0,Em alpha v,'
                                'Em v0 t,Em h v,Em h m,v0 m v,Em v0 m,v0 m t,'
                                'Em t v,Em h v0,m t v,v0 alpha m,v0 h m,'
                                'Em v0 v,Em m t,Em alpha m'),
        }
        self.possibilities_with_protected = {
            varsets_from_string('a b c,b c d,a b e,c f,d f g'):
            dict(
                ab=varsets_from_string('a b'),
                a=varsets_from_string('a b,a c,a e,a f'),
                b=varsets_from_string('a b,c b,b d,b e,b f'),
            )
                }

    def test_new_calculatable_return_proper_values(self):
        for equations in self.known_values:
            for calc_parts in self.known_values[equations]:
                calc = set()
                calc_parts.append(set())
                for i in range(len(calc_parts) - 1):
                    calc |= calc_parts[i]
                    # print(calc, calc_parts[i+1])
                    self.assertEqual(possibilities.new_calculatable(calc,
                                                                    equations),
                                     calc_parts[i+1])

    def test_calculatable(self):
        "calculatable() should return proper values"
        for equations in self.known_values:
            vars = set()
            for eq in equations:
                vars |= eq
            for calc_parts in self.known_values[equations]:
                calc = set()
                for part in calc_parts:
                    calc |= part
                self.assertEqual(possibilities.calculatable(calc_parts[0],
                                                            equations, vars),
                                 calc)

    def test_possibilities_can_be_called_with_two_arguments(self):
        for equations in self.possibilities:
            known_possibilities = set(self.possibilities[equations])
            possibilities_ = possibilities.possibilities(equations, [])
            # print(tuple(set(p) for p in possibilities_))
            self.assertEqual(set(possibilities_), known_possibilities)

    def test_possibilities_can_called_with_protected_variables(self):
        for equations, protected in self.possibilities_with_protected.items():
            for protected_variables, known_possibilities in protected.items():
                protected_variables = set(protected_variables)
                known_possibilities = set(known_possibilities)
                possibilities_ = possibilities.possibilities(
                    equations,
                    [],
                    protected_variables=protected_variables)
                # print(tuple(set(p) for p in possibilities_))
                self.assertEqual(set(possibilities_), known_possibilities)

    def test_possibilities_raise_exeption_if_too_many_protected_variables(self):
        equations = varsets_from_string('a b c,b c d,a b e,c f,d f g')
        for protected_variables in [set(i)
                                    for i in 'abc def fegd acdeg'.split()]:
            self.assertRaises(AssertionError,
                              possibilities.possibilities,
                              equations,
                              [],
                              protected_variables)


def suite():
    Possibilities_suite = unittest.makeSuite(TestPossibilities)
    TestGetVariables_suite = unittest.makeSuite(TestGetVariables)
    TestMakeEquations_suite = unittest.makeSuite(TestMakeEquations)
    TestHelperFunctions_suite = unittest.makeSuite(TestHelperFunctions)
    return unittest.TestSuite([Possibilities_suite,
                               TestGetVariables_suite,
                               TestMakeEquations_suite,
                               TestHelperFunctions_suite])


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__ == "__main__":
    test()
