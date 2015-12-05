#!/usr/bin/env python3

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


def main():
    if sys.argv[1] in ('help', '-h', '--help', '-help'):
        print(__doc__)
        sys.exit()
    code = int(sys.argv[-1])
    group = get_group()
    locals_ = {}
    exec('from varEC.%s import input_files' % group, globals(), locals_)
    input_files = locals_['input_files']
    print('input files:\n  ', end='')
    print(*input_files, sep='\n  ', end='\n\n')
    books = Books(input_files)
    text = books.exercise_text(code)
    exercise_test(text, variation_number=6, with_latextable=1)
