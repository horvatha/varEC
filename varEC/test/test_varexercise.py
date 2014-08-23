#!/usr/bin/env python3
# coding: utf-8

import unittest
import sys
import os
sys.path.append("/home/ha/ec/bin")

from varEC.varexercise import delete_remark, latextable_row
from varEC import varexercise


class TestDeleteRemark(unittest.TestCase):
    """Test the functions for extract table values."""

    def test_delete_remark(self):
        known_values = (
            # (r'  \\\\%alma', r'  \\\\'),
            (r' %alma', ' '),
            (r' körte%alma', r' körte'),
            (r' apple\\%körte%alma', r' apple'),
            (r' apple\%körte', r' apple\%körte'),
            (r' apple\\\%körte', r' apple\\\%körte'),
            # (r' apple\\\\%körte', r' apple\\\\'),
        )
        for arg, result in known_values:
            self.assertEqual(delete_remark(arg), result)


class TestLatexTable(unittest.TestCase):
    """Test the functions for creating LaTeX tables."""
    def test_latextable_row(self):
        known_values = (
            (('apple', 'banana', 'lime'), 'apple &banana &lime \\\\\n'),
            (('a', 'b', 'c'), 'a &b &c \\\\\n'),
        )
        for arg, result in known_values:
            self.assertEqual(latextable_row(arg), result)


class TestLatexNumber(unittest.TestCase):
    """Test the function latex_number"""
    def test_for_success(self):
        known_values = (
            (4.2e5, r"$4,2\cdot10^{5}$"),
            (3.60876e+04, r"$3,609\cdot10^{4}$"),
            (2.5e-009, r"$2,5\cdot10^{-9}$"),
            (3.4241200, r"3,424"),
            (2.4e-100, r"$2,4\cdot10^{-100}$"),
            (0.0000000324, r"$3,24\cdot10^{-8}$"),
        )
        for arg, result in known_values:
            self.assertEqual(varexercise.latex_number(arg), result)


class TestLatexFrame(unittest.TestCase):
    def test_for_success(self):
        text = ['This is a text.\n',
                'Its second row. (árvíztűrő tükörírógép)\n']
        expected_result = ['\\documentclass[a4paper, 11pt]{article}\n', '\n',
                           '\\usepackage{amsmath}', '\\begin{document}\n',
                           '\n', 'This is a text.\n',
                           'Its second row. (árvíztűrő tükörírógép)\n',
                           '\n', '\n\\end{document}\n']
        for class_argument in ("[a4paper, 11pt]", ):
            given_result = \
                varexercise.general_frame(text,
                                          class_argument=class_argument,
                                          preamble_text=r'\usepackage{amsmath}'
                                          )
            self.assertEqual(given_result, expected_result)


# TODO Copy these files to test directory?
class TestVariations(unittest.TestCase):
    def setUp(self):
        os.chdir('/home/ha/ec/')
        Variations = varexercise.Variations
        self.variations = [
            Variations([['A', 82, 781, '\\newpage'],
                        ['B', 785, 782]],
                       'optika.tex',
                       2),
            Variations([['Gauss', 101, 102, '\\newpage'],
                        ['Poisson', 103, 104]],
                       'valszam.tex',
                       2)
        ]

    def test_variation_can_be_framed_and_save(self):
        for variation in self.variations:
            framed = varexercise.frame(variation.one(1))
            with open('temp.tex', "w") as f:
                f.writelines(framed)
            # TODO Should be checked, the files can be translated into pdf.


if __name__ == "__main__":
    unittest.main()
