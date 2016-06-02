#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Makes the codes, where it's needed.
You must run it in the ec directory I think.
E.g:
python bin/ec-coder.py

Horváth Árpád, 2001. szeptember'''
from __future__ import print_function

from .common import _

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


def get_whole_name(file):
    file_names = name_with_path(file, file_paths)
    if file_names:
        return file_names[0]
    return None


def get_next_code(codelist, code_interval):
    start, stop = code_interval
    code = start
    while code in codelist:
        code += 1
        if code >= stop:
            raise ValueError(_(
                'There is no free code number! Ask for it!\n'
                '<horvath.arpad@amk.uni-obuda.hu>'))
    return code


def is_valid_code(code_string):
    return code_string.isdigit()


# TODO Should use ExerciseBook.bad_arguments_row_and_argument()
def new_codes(codelist, file_name, code_interval=code_interval):
    'Makes new codes for one file_name in the FILE_GROUP.'

    print('** file_name = %s' % file_name)
    if not os.path.isfile(file_name):
        print(_("There's no file named %s.") % file_name)
        return
    with open(file_name, 'r') as f:
        lines = f.readlines()

    # new lines
    new_lines = []

    beginfeladat = re.compile(r'''(\\ begin \s* \{ \s* feladat \s* }
             \{) (.*?) } \s*  ([^\s])?''', re.VERBOSE)
    change = 0
    path, basename = os.path.split(file_name)
    for line in lines:
        begin = re.search(beginfeladat, line)
        if begin and not is_valid_code(begin.group(2)):
            # if there is something after the code number
            if begin.group(3):
                newpattern = r'\g<1>%d}  \g<3>\n'
            else:
                # if there is nothing after the code number
                newpattern = r'\g<1>%d}\n'
            change += 1  # One more changes
            code = get_next_code(codelist, code_interval)
            new_lines.append(beginfeladat.sub(newpattern % code, line))
            print(_('\tnew code number: %d') % code)
            codelist.append(code)
            write_logfile(code, basename, path)

        else:
            new_lines.append(line)

    if change == 0:
        print(_('\tThere wasn\'t any changes in this file.'))
        return codelist

    archive_file = os.path.join(path, 'old_' + basename)
    print(_('\tThere was %d changes in this file.') % change)

    if os.path.islink(file_name):
        shutil.copyfile(file_name, archive_file)
        path, basename = os.path.split(file_name)
        link = os.path.join(path, os.readlink(file_name))
        print(link)
        file_name = os.path.abspath(link)
    else:
        os.rename(file_name, archive_file)
    with open(file_name, 'w') as f:
        f.writelines(new_lines)
    print(_('!\tThe new file is in %s\n!\tthe original is in %s.')
          % (file_name, archive_file))

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
    print(_('Book Shelf="%s"') % FILE_GROUP)
    print(_('If it isn\'t good, '
          'set it in the bin/setup_hu.py file (at the beginning).'))
    answer = input(_('May I continue? (Y/n) '))
    if answer in ('n', 'N'):
        print(_('Good bye!'))
        return
    from varEC import books

    locals_ = {}
    exec('from varEC.courses.%s import input_files' % FILE_GROUP, locals_)
    input_files = locals_.get('input_files')
    if isinstance(input_files, str):
        input_files = [input_files]

    print(_('The files of this Book Shelf are: %s') % ", ".join(input_files))

    books = books.BookShelf(input_files)
    codelist = books.codelist()
    print(_("There are {exercises} exercises "
          "in the {books} Exercise Book on this Bookshelf.")
          .format(exercises=len(codelist), books=len(books.books)))
    integer_codes = [c for c in codelist if isinstance(c, int)]
    print(_("Code list:"), integerlist.IntegerList(integer_codes))
    not_unique_codes = integerlist.IntegerList(
        integerlist.search_not_uniq(integer_codes).keys()
    )
    if not_unique_codes:
        print(_("Not unique codes:"), not_unique_codes)
    for code in not_unique_codes:
        print(_("I have found code {} here:").format(code))
        places_of_code(books, code)

    bad_args = books.exercises_with_bad_arguments()
    if bad_args:
        print(_("Bad arguments are in the files below:"))
        for tuple_ in bad_args:
            print(_("In file {} in the row {}"
                    " the argument is '{}'").format(*tuple_))

    for file in books.files_with_bad_arguments():
        whole_name = get_whole_name(file)
        if whole_name:
            codelist = new_codes(codelist, whole_name)
        else:
            print(_("There is not file named %s.") % file)

    for file in input_files:
        whole_name = get_whole_name(file)
        checksolution(whole_name)
