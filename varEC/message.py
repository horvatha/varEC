#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This modul is for the unified appearance.

message use write for handling several-line-string
"""

from . import lang

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
    new_message('A következő fájlt kiírtam: %s.' % "testpaper.tex")
    print()
    new_message('Ez itt az üzenet.')
    print()

if __name__ == '__main__':
    test()
