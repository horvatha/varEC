#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Makes the codes, where it's needed.
You must run it in the ec directory I think.
E.g:
python bin/ec-coder.py

Horváth Árpád, 2001. szeptember'''
from __future__ import print_function

from varEC.message import error

# You may write new row after these
# or put the item you need to the end of this queue.
FILE_GROUP = 'mat'
FILE_GROUP = 'fizika'
from varEC.setup_hu import FILE_GROUP, code_interval, file_paths
from varEC.books import name_with_path
from varEC import integerlist

try:
    input = raw_input
except NameError:
    pass

import re
import os
import shutil
import time
from varEC import lang


def whole_name(file):
    file_names = name_with_path(file, file_paths)
    if file_names:
        return file_names[0]
    return None


def not_integer(string):
    try:
        int(string)
    except ValueError:
        return 1
    return 0


# TODO Should use ExerciseBook.bad_arguments_row_and_argument()
def new_codes(codelist=[],
              file=None,
              code_interval=code_interval,
              archive_file=None):
    'Makes new codes for one file in the FILE_GROUP.'

    print('** file_name = %s' % file)
    if not os.path.isfile(file):
        print("There's no file named %s." % file)
        return
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    # new lines
    new_lines = []

    beginfeladat = re.compile(r'''(\\ begin \s* \{ \s* feladat \s* }
             \{) (.*?) } \s*  ([^\s])?''', re.VERBOSE)
    code = code_interval[0]
    change = 0
    for line in lines:
        begin = re.search(beginfeladat, line)
        if begin and not_integer(begin.group(2)):
            # if there is something after the code number
            if begin.group(3):
                newpattern = r'\g<1>%d}\n\g<3>'
            else:
                # if there is nothing after the code number
                newpattern = r'\g<1>%d}\n'
            change += 1  # One more changes
            while code in codelist:
                code += 1
                if code >= code_interval[1]:
                    error('code run out')
                    return codelist
            new_lines.append(beginfeladat.sub(newpattern % code, line))
            print('\tnew code number: %d' % code)
            codelist.append(code)
            path, basefile = os.path.split(file)
            write_logfile(code, basefile, path)

        else:
            new_lines.append(line)

    if change == 0:
        print('\tThere wasn\'t any changes in this file.')
        return codelist

    if (not archive_file) or (archive_file == file):
        path, basename = os.path.split(file)
        archive_file = os.path.join(path, 'old_' + basename)
    print('\tThere was %d changes in this file.' % change)

    if os.path.islink(file):
        shutil.copyfile(file, archive_file)
        path, basename = os.path.split(file)
        link = os.path.join(path, os.readlink(file))
        print(link)
        file = os.path.abspath(link)
    else:
        os.rename(file, archive_file)
    f = open(file, 'w')
    f.writelines(new_lines)
    f.close()
    print('!\tThe new file is in %s\n!\tthe original is in %s.'
          % (file, archive_file))

    return codelist


def write_logfile(code, basefile, path):
    localtime = time.localtime(time.time())
    date = time.strftime("%Y %m %d", localtime)

    f = open(os.path.join(path, '%s_group.log' % FILE_GROUP), 'a')
    f.writelines(['%d   %s      %s\n' % (code,
                                         basefile,
                                         date)])
    f.close()


def checksolution(file, lang=lang.lang):
    if lang == "en":
        env = "solution"
    elif lang == "hu":
        env = "megoldas"
    pattern = r"(\s*)\\end{megoldas}"
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    for row, line in enumerate(lines):
        result = re.search(pattern, line)
        if result and result.group(1) != "":
            print(r"!!! There should not be any spaces before \end{{{0}}} "
                  "in the file {1} in row {2}".format(env, file, row+1))


def places_of_code(books, code):
    exercises = books.get_exercises(code)
    for file_name, exercise in exercises:
        print("\t{file_name} line {exercise.begin.row}".format(**locals()))


def main():
    '''Makes new codes for the files in the input_files in a FILE_GROUP.
    input_files can be a file name or a file name list
    FILE_GROUP is constant at the beginning of this file.'''
    print('Book Shelf="%s"' % FILE_GROUP)
    print('If it isn\'t good, '
          'set it in the bin/setup_hu.py file (at the beginning).')
    answer = input('May I continue? (Y/n) ')
    if answer in ('n', 'N'):
        print('Good bye!')
        return
    from varEC import books

    locals_ = {}
    exec('from varEC.%s import input_files' % FILE_GROUP, locals_)
    input_files = locals_.get('input_files')
    if isinstance(input_files, str):
        input_files = [input_files]

    print('The files of this Book Shelf are: %s' % ", ".join(input_files))

    books = books.Books(input_files)
    codelist = books.codelist()
    print("There are {exercises} exercises "
          "in the {books} Exercise Books of this Book Shelf."
          .format(exercises=len(codelist), books=len(books.books)))
    integer_codes = [c for c in codelist if isinstance(c, int)]
    print("Code list:", integerlist.IntegerList(integer_codes))
    not_unique_codes = integerlist.IntegerList(
        integerlist.search_not_uniq(integer_codes).keys()
    )
    if not_unique_codes:
        print("Not unique codes:", not_unique_codes)
    for code in not_unique_codes:
        print("I have found code {} here:".format(code))
        places_of_code(books, code)

    for file in input_files:
        _whole_name = whole_name(file)
        # print("_whole_name:", _whole_name)
        if _whole_name:
            codelist = new_codes(codelist, _whole_name)
        else:
            print("There is not file named %s." % file)

        checksolution(_whole_name)
