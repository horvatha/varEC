# encoding: utf-8
from __future__ import print_function
"""
#####################################################
##
##     Searching for exercises and intervals
##
#####################################################
It is the part of the "ec" program group.

class Books, ExerciseBook
  searches and stores exercises in an exercise-book or in a testpaper

def name_with_path(file, file_paths): --> occurence_list
  It searches for the file in 'file_paths' directory list.
  It gives back all the 0 or more occurences in a list.

"""

from .lang import env
from .setup_hu import file_paths
from .message import print_text
from .common import BadCodeException

import re
import os


def name_with_path(file, directories):
    """It searches for the file in a directory list.
    It gives back all the 0 or more occurences in a list.
    """

    name_list = []
    for path in directories:
        whole_name = os.path.join(path, file)
        if os.path.isfile(whole_name):
            name_list.append(whole_name)
    return name_list


def read_files_lines_or_empty_list(file):
    if not os.path.isfile(file):
        return []
    with open(file) as f:
        lines = f.readlines()
    return lines


def _name_with_path_test(file):
    print(name_with_path(file, ['.', '../matematika_hu', '../zh']))


class Place:
    def __init__(self, row, start, end):
        self.row = row
        self.start = start
        self.end = end

    def __str__(self):
        return "In row %d, spans from %d to %d" % (self.row,
                                                   self.start,
                                                   self.end)


class Interval:
    def __init__(self, row, start, end, name, interval):
        self.place = Place(row, start, end)
        self.name = name  # Here can be a formula too.
        self.interval = interval

    def __str__(self):
        str = "{{Interval interval:%s row:%d name:%s }}" % (self.interval,
                                                            self.place.row,
                                                            self.name or '-')
        return str


class Environment:
    """ A class for store the structure of  environment exercise and
 (exercise)group"""

    def __init__(self, row, start, end, type='exercise'):
        self.begin = Place(row, start, end)
        self.type = type
        self.num = None
        self.section_number = None
        if type == 'group':
            self.exercises = []

    def add_end(self, row, start, end):
        self.end = Place(row+1, start, end)

    def __str__(self):
        if self.type == 'exercise':
            return "Exercise %4s is the %3d-th in section %2d from the row %4d." % \
                (self.code, self.num, self.section_number, self.begin.row)
        elif self.type == 'group':
            intv_num = len(self.exercises)
            return '//Exercise-group with %d exercises from row %d.//' %\
                (intv_num, self.begin.row)


class Books:
    """ Class for handle a collection of exercise books."""
    def __init__(self,
                 file_names,
                 file_type='exercise series',
                 ):
        if isinstance(file_names, str):
            file_names = [file_names]
        self.file_names = file_names
        self.file_type = file_type
        self.books = []
        self.get_books()

    def __str__(self):
        str = ''
        for book in self.books:
            str += book.__str__()
        return str

    def get_books(self):
        "Get the date of the books at initialization."
        for file_name in self.file_names:
            self.books.append(
                ExerciseBook(file_name, file_type=self.file_type)
            )

    def exercise_text(self, code):
        """Returns with the text of exercise or None."""
        for book in self.books:
            text = book.exercise_text(code)
            if text:
                return text
        return []

    def codelist(self):
        """ It returns with all the codes in the books."""
        codelist = []
        for book in self.books:
            codelist += book.code_list
        return codelist

    def code_container_books(self, code):
        """ It returns with the books, which has the code."""
        return [book for book in self.books if code in book.code_list]

    def get_exercises(self, code):
        """Get the exercises of the codes to check
        wheter there is multiple occurence."""
        exercise_list = []
        for exercise_book in self.books:
            for i, code_list in enumerate(exercise_book.code_list):
                if code is code_list:
                    exercise_list.append(
                        (exercise_book.file_name, exercise_book.exercises[i])
                    )
        return exercise_list

    def exercises_with_bad_arguments(self):
        """ Returns with a list of the tuple (filename, row, argument). """
        exercise_list = []
        for book in self.books:
            delta_list = [
                (book.file_name, item[0], item[1])
                for item in book.bad_arguments_row_and_argument()
            ]
            exercise_list.extend(delta_list)
        return exercise_list

    def definitions(self, codes=None):
        """ Returns with the definitions in all the books
        or in the books that contains minimum one of the code in codes."""
        definition_list = []

        if codes:
            booklist = []
            for code in codes:
                booklist.extend(self.code_container_books(code))
            book_file_names = set([book.file_name for book in booklist])

        for book in self.books:
            if codes:
                if book.file_name not in book_file_names:
                    return
            definition_list += book.definitions()
        return definition_list


class ExerciseBook:
    """ Class for storing the structure (and making several testpapers)."""

    def __init__(self,
                 file_name,
                 file_type='exercise series',
                 **kwargs):
        """  filenames: is a list of filenames or a filename in a string
        file_type is 'exercise series' or 'testpaper' """

        self.file_name = file_name
        self.file_paths = file_paths
        self.type = file_type
        self.exercises = []
        self.sections = []  # It can be sections or groups.
        self.groups = []  # It stores exercisegroup-environments
        text = kwargs.pop('text', [])
        assert not kwargs
        self.lines = self.text_loader(text)
        self.set()

    def text_loader(self, text):
        if text:
            return text
        whole_name = name_with_path(self.file_name, self.file_paths)[0]
        lines = read_files_lines_or_empty_list(whole_name)
        return lines

    def __str__(self):
        str = ' Exercise book "%s"\n' % self.file_name
        for exercise in self.exercises:
            str += '\t%s\n' % exercise.__str__()
        return str

    def set(self):
        "Searches for exercises and intervals."

        # Patterns

        beginp = re.compile(
            r"\\begin \s* \{\s*"+env['exercise']+r"\s*} \s* {(.*?)}",
            re.VERBOSE)
        endp = re.compile(r"\\end\s*\{\s*"+env['exercise']+r"\s*}", re.VERBOSE)

        groupbeginp = re.compile(r"\\begin\s*\{\s*" + env['group'] + r"\s*}",
                                 re.VERBOSE)
        groupendp = re.compile(
            r"\\end\s*\{\s*"+env['group']+r"\s*}", re.VERBOSE)
        # intervalp = re.compile(
        #     r"\\interval\s*(\[\s*([^\]]*)\s*]\s*)?"
        #     "{\s*([^}]*)\s*}{\s*([^}]*)\s*}")

        if self.type == 'testpaper':
            sectionp = re.compile(r'\\group \s* \{ ([^}]*) }', re.VERBOSE)
        elif self.type == 'exercise series':
            sectionp = re.compile(r'\\section\*?\s*\{([^}]*)}', re.VERBOSE)
        else:
            raise TypeError('bad Structure type')

        state = 'not in exercise'
        exercise_number = 0
        section_number = 0  # Section is testgroup in testpapers.
        group_number = 0  # The serial number of the group environment.
        is_in_group = 0
        for row in range(1, len(self.lines)+1):
            line = self.lines[row-1]  # The index of the 1-st row is 0, etc.!

            if state == 'not in exercise':
                # It found a new section
                section = sectionp.search(line)
                if section:
                    self.sections.append(section.group(1))
                    section_number = section_number + 1
                    exercise_number = 0

                # It found the begin of an exercise environment
                begin = beginp.search(line)
                if begin:
                    exercise_number = exercise_number + 1
                    exercise = Environment(row, begin.start(), begin.end())
                    exercise.num = exercise_number
                    exercise.section_number = section_number
                    raw_code = begin.group(1)
                    try:
                        exercise.code = int(raw_code)
                    except ValueError:
                        exercise.code = raw_code
                        if raw_code != "":  # TODO Find a better solution.
                            raise BadCodeException(
                                self.file_name, exercise.code, row)
                    if is_in_group:
                        group_env.exercises.append(exercise.code)
                    state = 'in exercise'

                # It found the begin of an exercise-group environment
                groupbegin = groupbeginp.search(line)
                if groupbegin:
                    is_in_group = 1
                    group_number = group_number + 1
                    group_env = Environment(row, groupbegin.start(),
                                            groupbegin.end(), 'group')
                groupbegin = groupbeginp.search(line)

                # It found the end of an exercise-group environment
                groupend = groupendp.search(line)
                if groupend:
                    is_in_group = 0
                    group_env.add_end(row, groupend.start(), groupend.end())
                    self.groups.append(group_env)

            elif state == 'in exercise':
                start = None

                # It found the end of an exercise environment
                end = endp.search(line)
                if end:  # start is the start column of the last interval
                                # or None if there weren't any interval
                    if start and start > end.start():
                        # 'start' is the start column of the last interval
                        # or None if there weren't any interval
                        raise ValueError(
                            'there is \end{exercise} before the last \interval')
                    else:
                        exercise.add_end(row, end.start(), end.end())
                        self.exercises.append(exercise)
                        state = 'not in exercise'

        self.codelist_maker()

    def print_groups(self):
        if not self.groups:
            print('No groups in "%s".' % self.file_name)
            return
        for group in self.groups:
            print(group.__str__())

    def codelist_maker(self):
        self.code_list = [ex.code for ex in self.exercises]

    def bad_arguments_row_and_argument(self):
        return [(ex.begin.row, ex.code) for ex in self.exercises
                if not isinstance(ex.code, int)]

    def test(self):
        ex = self.exercises[1]
        print('Exercise %d' % ex.code)
        print_text(self.exercise_text(ex.code))
        print(ex)
        print

    def exercise_text(self, code, solution=True):
        """ Returns with the text of the exercise.
        If it doesn't exists it returns with None.
        If solution = False, it returns without solution."""
        if code not in self.code_list:
            return None
        exercise = self.exercises[self.code_list.index(code)]
        text = self.lines[exercise.begin.row-1:exercise.end.row-1]
        return text if solution else self.without_solution(text)

    @staticmethod
    def without_solution(text):
        """ It will delete the solution-part of the exercise."""
        return text  # TODO

    def definitions(self):
        """ Returns with the definitions in the book."""
        begin = r"%begin\{definitions?}"
        end = r"%end\{definitions?}"

        definition_lines = []
        state = 'search'
        for line in self.lines:
            if state == 'search':
                s = re.search(begin, line)
                if s:
                    state = 'write'
            elif state == 'write':
                s = re.search(end, line)
                if s:
                    definition_lines.append('\n')
                    state = 'search'
                else:
                    definition_lines.append(line)
        return definition_lines


if __name__ == "__main__":
    _name_with_path_test("analizis.tex")
