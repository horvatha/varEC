#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This modul is for the unified appearance.

error and message use write for handling several-line-string
menu and ask is independent from write

They all get the strings from nationalized lang module (lang_en, lang_hu)
"""
from . import lang

try:
    command = 'from . import lang_%s' % lang.lang
    exec(command)
    command = 'lang = lang_%s' % lang.lang
    exec(command)
except ImportError:
    from . import lang_en
    lang = lang_en
    del lang_en

# try:
#   command = 'import setup_%s' % lang.lang
#   exec(command)
#   command = 'setup = setup_%s' % lang.lang
#   exec(command)
# except ImportError:
#   import setup_en
#   setup = setup_en
#   del setup_en


def write(string, arguments=None,
          starting_characters=''):
    if arguments:
        string = string % arguments

    rows = string.split('\n')
    if not rows[-1]:
        rows.pop()

    n = 0
    for row in rows:
        row = '%s %s' % (starting_characters, row)
        rows[n] = row
        n = n + 1

    for row in rows:
        print(row)


def error(error_code, arguments=None):
    write(lang.err[error_code], arguments, '!!!')


# new message translated by gettext
def message(message):
    write(message, None, '>>>')


def cls():
    'It clears the screen. Or do something between actions.'
    print('\n'*5)
    # os.system('clear')


def print_text(text):
    for line in text:
        if line[-1:] == "\n":
            line = line[:-1]
        print(line)


def test():
    write('error\n in row %d\n', 15, '!!!')
    print()
    error('bad code', 77)
    print()
    new_message('A következő fájlt kiírtam: %s.' % "testpaper.tex")
    print()
    new_message('Ez itt az üzenet.')
    print()

if __name__ == '__main__':
    test()
