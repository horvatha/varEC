#!/usr/bin/env python3
# coding: utf-8

import unittest
import sys
import os
sys.path.append("/home/ha/ec/bin")
import collections

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


list_attributes = [
    'interval_list', 'compute_list', 'const_list',
    'protected_variables', 'ecChoose_list']

TextData = collections.namedtuple('Text',
                                  (['text'] + list_attributes +
                                   ['first_compute_row']))
texts = dict(
    text_sin=TextData(r"""
    Határozza meg annak a testnek a sebesség és gyorsulásfüggvényét,
    amelynek a helyzetét az\\
    $x= At^2 +1\mathrm{m}\cdot \sin Ct$ \quad függvény írja le,
    ahol
    \[A= \interval{3}{!A=4..10} \dfrac m{s^2},
    C= \interval{6}{!C=3..9}\, \dfrac1s\]
    A test gyorsulása a $t=\interval{6}{!t=1..12}$~s pillanatban
    \compute[$m/s^2$]{a=2*A - C*C*sin(C*t)}.
    """.splitlines(keepends=True),
        3, 1, 0,
        3,
        0,
        9,
        ),
    text_acos=TextData(r"""
    Egy \interval[m]{53}{!h=40..121} magas toronyból, mely körül a terep sík,
    vízszintesen \interval[m/s]{5}{v0=5.1..20} sebességgel lőnek ki egy
    \interval[kg]{4}{m=2.01..5} tömegű ágyúgolyót.
    A golyó \compute[s]{t=sqrt(2*h/g)} múlva csapódik a földbe
    \compute[m/s]{v=sqrt(v0**2+(g*t)**2)} sebességgel,
    \compute{alpha=acosd(v0/v)}~$^0$-os szög alatt a vízszinteshez
    képest.
    A becsapódáskor a mozgási energiája \compute[J]{E=0.5*m*v*v}.
    """.splitlines(keepends=True),
        3, 4, 0,
        1,
        0,
        5,
        )
)


def get_exercise_and_text_data(text_name, number_of_variations=5):
    text_data = texts[text_name]
    exercise = varexercise.VarExercise(text_data.text,
                                       77,
                                       number_of_variations)
    return exercise, text_data


def test_lengths_of_list_attribute(test_case, text_name):
    """docstring for test_list_length"""
    exercise, text_data = get_exercise_and_text_data(text_name)
    for attribute_name in list_attributes:
        attr = getattr(exercise, attribute_name)
        value = getattr(text_data, attribute_name)
        test_case.assertEqual(len(attr), value)


def test_first_compute_row(test_case, text_name):
    """docstring for test_list_length"""
    exercise, text_data = get_exercise_and_text_data(text_name)
    test_case.assertEqual(exercise.compute_list[0]['row'],
                          text_data.first_compute_row)

import math


class TestVarExercise(unittest.TestCase):
    def test_texts_have_proper_attributes(self):
        for text_name in texts:
            test_lengths_of_list_attribute(self, text_name)
            test_first_compute_row(self, text_name)

    def test_exercise_values(self):
        exercise, _ = get_exercise_and_text_data('text_acos')
        self.assertGreater(len(exercise.list), 0)
        for values, erased_elements in exercise.list:
            g = 9.81
            h = values.get('h')
            self.assertTrue(40 <= h <= 121)
            v0 = values.get('v0')
            m = values.get('m')
            t = math.sqrt(2*h/g)
            self.assertAlmostEqual(values.get('t'), t)
            v = math.sqrt(v0**2+(g*t)**2)
            self.assertAlmostEqual(values.get('v'), v)
            alpha = math.acos(v0/v)*180/math.pi
            self.assertAlmostEqual(values.get('alpha'), alpha)
            E = 0.5*m*v*v
            self.assertAlmostEqual(values.get('E'), E)


if __name__ == "__main__":
    unittest.main()
