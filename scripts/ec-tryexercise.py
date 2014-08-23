#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function

""" Usage: ec-tryexercise.py [group] code
It makes several variations for the exercise
so you can test it.
"""

import sys
from varEC.books import Books
from varEC.varexercise import exercise_test

def get_group():
    if len(sys.argv) < 3:
        from varEC.setup_hu import FILE_GROUP
        return FILE_GROUP
    else:
        return sys.argv[1]

code = int(sys.argv[-1])
group = get_group()
exec('from varEC.%s import input_files' % group)
print('input files:\n  ', end='')
print(*input_files, sep='\n  ', end='\n\n')
books = Books(input_files)
text = books.exercise_text(code)
exercise_test(text, variation_number=6, verbose=0, with_latextable=1)
