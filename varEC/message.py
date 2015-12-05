#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This modul is for the unified appearance.

error and message use write for handling several-line-string
menu and ask is independent from write

They all get the strings from nationalized lang module (lang_en, lang_hu)
"""
from __future__ import print_function

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


def message(message_code, arguments=None):
    write(lang.mesg[message_code], arguments, '>>>')


def ask_exit(next_to_do):
    """ It asks wether to continue or not """
    print('*'*30)
    print("%s %s." % (lang.mesg['next'], lang.todo[next_to_do]))
    answer = 'not valid value'
    while answer != '' and answer not in lang.keys['quit']:
        answer = input(ask('enter'))
        print()
    if answer == '':
        cls()

        print('******** %s.' % lang.todo[next_to_do])
        return 0
    if answer in lang.keys['quit']:
        return 1


def cls():
    'It clears the screen. Or do something between actions.'
    print('\n'*5)
    # os.system('clear')


def menu():
    menu_list = lang.menu_list

    n = 1
    for item in menu_list:
        print(' %2d. %s.' % (n, item[1]))
        n = n + 1

    n = ask_integer(ask('choice'), 1, n-1)
    cls()
    return menu_list[n-1][0]


def ask_integer(_message, min=None, max=None):
    while True:
        num = input(_message)
        try:
            num = int(num)
        except ValueError:
            error('not_num')
            continue
        if min and num not in range(min, max+1):
            error('bad_value')
            continue
        return num


def get_integer(ask_code, max=None, min=None):
    """ Returns with a number between min and max. """

    if max < min:
        raise ValueError('max is less than min')

    while True:
        try:
            num = int(input(ask(ask_code)))
        except ValueError:
            error('not_num')
            continue
        if min and num < min:
            error('small num', min)
            continue
        if max and num > max:
            error('large num', max)
            continue
        return num


def ask(ask_code, arguments=None):
    if arguments:
        string = lang.ask[ask_code] % arguments
    else:
        string = lang.ask[ask_code]
        string = "%s " % string
        return string


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
    message('file_written', "testpaper.tex")
    print()
    message('with solution')
    print()
    function = menu()
    print("\nFunction is '%s'." % function)

if __name__ == '__main__':
    test()
