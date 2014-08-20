#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from question_set_creator import latex_tools

""" This is a module for ec programs. It makes several variations
 for an exercise (class VarExercise).
 It can list the variations in an ASCII table or a LaTeX list.

 class Variations can make one or more testpapers.
 See Variations.one.__doc__
     Variations.all.__doc__
     Variations.list.__doc__
     Variations.solution.__doc__
     frame.__doc__

 See http://www.arek.uni-obuda.hu/harp/latex/ec
"""
# bug list at ec-sorter.py

from lang import lang
from ec_message import error, print_text
from varEC import possibilities


class LaTeXError(Exception):
    def __init__(self, type_, code, row):
        self.type_ = type_
        self.code = code
        self.row = row

    def __str__(self):
        return """There is a bad %s in the exercise %s!
The format is %s{<base_value>}{<xxx>} and must be in one row!
The row is:
 %s""" % (self.type_, self.code, self.type_, self.row)


class EcSyntaxError(Exception):
    def __init__(self, row):
        self.row = row

    def __str__(self):
        return """There is a syntax error in the table
in the row {0}.""".format(self.row)

try:
    exec('from setup_%s import decimal_point, times, FILE_GROUP' % lang)
except ImportError:
    print("I use english instead of %s." % lang)
    from setup_hu import decimal_point, times, FILE_GROUP
try:
    exec('from lang_%s import mesg, err, dictionary' % lang)
except ImportError:
    print("I use english instead of %s." % lang)
    from lang_en import dictionary

# TODO Not a nice solution, we should get the wide from "bin/%s.py" % FILE_GROUP
if FILE_GROUP in ["szamtudmat", "hiradastechnika", "informatika", "mat", "fizika"]:
    wide = True
else:
    wide = False

import re
import random
import itertools

import interval
interval_ = interval
del interval

import math
from math import sin, cos, asin, acos, tan, atan, sqrt, log, log10, exp, sinh, cosh, tanh, pi
# Trigonometrical functions. They calculate with degrees.
# The name is same as the original, but ended with 'd'.
def sind(x): sin(pi/180*x)
def cosd(x): cos(pi/180*x)
def tand(x): tan(pi/180*x)
def asind(x): 180/pi*asin(x)
def acosd(x): 180/pi*acos(x)
def atand(x): 180/pi*atan(x)
# TODO Why don't work they correctly in exercises?


from books import Books, ExerciseBook


class Variations:
    """ Makes the variations for the exercise_numbers, and its methods
  returns with the LaTeX texts without a frame
  (that means without preamble and {document} environment)."""
    def __init__(self,
                 exercise_numbers,
                 file_names,
                 number_of_variations,
                 verbose=0
                 ):

        self.exercise_numbers = exercise_numbers[:]
        self.verbose = verbose
        self.varexercise_numbers = exercise_numbers[:]
        if isinstance(file_names, str):
            file_names = [file_names]
        self.number_of_variations = number_of_variations
        self.books = Books(file_names, verbose=self.verbose - 1)
        self.all_code_exists = 1
        self.make_varexercises(number_of_variations)
        self.variable_list = None

    def make_varexercises(self, number):
        """Makes varexercises using book, and makes varexercise_numbers.
        Its structure is like structure of exercise_numbers,
        but varexercises replaces codes."""

        for group_number in range(len(self.varexercise_numbers)):
            for item_number in range(1, len(self.varexercise_numbers[group_number])):
                item = self.varexercise_numbers[group_number][item_number]
                if isinstance(item, int):
                    code = item
                    if not self.books.code_container_books(code):
                        error('exercise missing', code)
                        self.all_code_exists = 0
                    text = self.books.exercise_text(code)
                    vvar = VarExercise(text,
                                       code,
                                       number)
                    self.varexercise_numbers[group_number][item_number] =\
                        vvar
                    if vvar.is_interval():
                        self.is_interval = True

        # print('self.varexercise_numbers = %s ' % self.varexercise_numbers

    def one_group(self, number=0, group_number=1):
        '''Returns with the number-th variation of the group_number-th group.'''
        text = []
        group = self.varexercise_numbers[group_number-1]
        base_groupname = group[0]
        if number == 0:  # the original form of exercises
            groupname = base_groupname
        else:
            groupname = '%s$_{%d}$' % (base_groupname, number)
        text.append('\n\n\\group{%s}\n' % groupname)
        for item in group[1:]:
            text.append('\n\n')
            if isinstance(item, str):
                # It is a text, I insert it to the text.
                text.append(item)
            else:
                varexercise = item
                if number == 0:  # The base text
                    exercise_text = varexercise.text
                else:
                    exercise_text = varexercise.vartext(number-1) or\
                        varexercise.text
                text.extend(exercise_text)
        return text

    def one(self, number=0, frame=0):
        """Returns with the text of number-th variation
  (without the {document} environment).
  Number is in 1..number_of_variations
  If number == 0, it will use the original form of the exercises.
  (In VarExercise it is 0..number_of_variations-1)"""

        text = []
        for group_number in range(1, len(self.varexercise_numbers)+1):
            text.extend(
                self.one_group(number=number, group_number=group_number)
            )

        return text

    def all(self, frame=0):
        r""" Returns with the text of all variations in one text
       separated with \newpage"""
        text = []
        for number in range(1, self.number_of_variations+1):
            text.extend(self.one(number))
            text.append('\n\n\\newpage')
        return text

    def definitions(self, num, frame=0):
        """Returns with the definitions of num-th variation."""
        pass
        # TODO

    def group_list(self, group_number=1, with_solution=True):
        """ Returns with the values of the variations of a group as a latex text.
        If there is no variations, it returns with empty string ("")."""
        text = []
        group = self.varexercise_numbers[group_number-1]
        group_name = dictionary['group_name'] % group[0]
        text.append('\n\\subsection*{%s}\n' % group_name)
        for number in range(1, self.number_of_variations+1):
            print(number)  # !!!
            variation = '\n\n\\textbf{%s}\\\\\n' %\
                        dictionary['variation'] % number
            text.append(variation)
            exercise_number = 1
            for item in group[1:]:
                print(' '*5, item)  # !!!
                if not isinstance(item, str):
                    latex_plain = item.latex_plain(number)
                    if latex_plain:
                        text.append('%d. ' % exercise_number)
                        print(' '*5, number)  # !!!
                        print(' '*5, latex_plain)  # !!!
                        text.append(latex_plain + '\n')
                    exercise_number += 1
        if with_solution:
            text.extend(self.one_group(group_number=group_number))
            text.append("\\newpage\n")
        return text

    def list(self, frame=0, with_solution=True):
        """ Returns with the values of the variations as a latex text.
        If there is no variations, it returns with empty string ("")."""
        text = []
        if not self.number_of_variations:
            return ""
        for group_number in range(1, len(self.varexercise_numbers)+1):
            text.extend(
                self.group_list(group_number, with_solution=with_solution))
        return text

    def groups(self):
        """Returns with a fancy ASCII format of the groups."""
        groups_text = '\n'
        for group in self.exercise_numbers:
            txt = ' %s:\t' % group[0]
            for exercise in group[1:]:
                if isinstance(exercise, int):
                    txt += '%d. ' % exercise
                else:
                    txt += '\n\t%s\n\t' % exercise
            groups_text += txt + '\n'
        return groups_text


def _variation_test():
    v = Variations([['A', 784, '\\newpage', 781, '\\newpage'], ['B', 785, 782]],
                   'optika.tex',
                   3)
#     v = Variations([['A', 101, 102, '\\newpage'], ['B', 103, 104]],
#                    'valszam.tex',
#                    2)
    print("1"*50)
    print(print_text(v.one(1)))
    print()
    print("2"*50)
    print(print_text(v.one(2)))
    print()
    print("3"*50)
    print(print_text(v.one(3)))
    print()
    print("var "*12)
    print(print_text(v.list()))


def frame(text,
          preamble_file = 'magyarpreambulum',
          pagesize = 'a4paper',
          fontsize = 11,
          lhead = '-',
          rhead = '-',
          lfoot = '-',
          rfoot = '-',
          cfoot = None,
          definitions = None,
          doc_type = 'testpaper',
          ):

    """ It will give the frame of the testpapers.
    It makes preambulum and \\begin{document}... """

    preamble_text = []
    preamble_text.append(dictionary['doctype comment'])
    preamble_text.append('\\newcommand{\doctype}{%s}\n' % doc_type)

    preamble_text.append('''
\\usepackage{ucs}
\\usepackage[utf8x]{inputenc}
\\newcommand{\groupname}{}
\n''')

    if wide:
        preamble_text.append(r"""\voffset -1. cm
\textheight 24cm
\hoffset -1.2 cm
\textwidth 17cm
\headheight -3. cm
%\footheight 1.5cm
\oddsidemargin 3mm
\topskip 7mm
\parskip 3mm
\parindent 1cm
\baselineskip 6mm
""")

    preamble_text.append(r"""
%% FEJ és LÁBLÉC
%%%%%%%%%%%%%%%%%%%%%
\usepackage{fancyhdr}
\pagestyle{fancy}
""")

    if lhead:
        preamble_text.append("\\lhead{%s}\n" % lhead)
    if rhead:
        preamble_text.append("\\rhead{%s}\n" % rhead)
    if lfoot:
        preamble_text.append("\\lfoot{%s}\n" % lfoot)
    if rfoot:
        preamble_text.append("\\rfoot{%s}\n" % rfoot)
    if cfoot:
        preamble_text.append("\\cfoot{%s}\n" % cfoot)
    else:
        preamble_text.append("\\cfoot{\\groupname}\n")
    preamble_text.append("\n")

    if preamble_file:
        preamble_text.append("\\input{%s}\n" % preamble_file)
        preamble_text.append('\n')

    if definitions:
        if definitions[-1] == "\n":
            definitions = definitions[:-1]
        preamble_text.append("%begin{definitions}\n")
        preamble_text.extend(definitions)
        preamble_text.append("%end{definitions}\n")
        preamble_text.append("\n")

    preamble_text.append(r'''\input{formats}

% Itt esetleg állíthatod a többi logikai változót. (def_hu.tex)

\input{commands_hu}''')

    if fontsize not in [10, 11, 12]:
        if type == 'list':
            fontsize = 10
        else:
            fontsize = 11

    return general_frame(text,
                         class_argument='[%s, %dpt]' % (pagesize, fontsize),
                         preamble_text=preamble_text)


def _frame_test():
    v = Variations([['A', 784, 781, '\\newpage'], ['B', 785, 782]],
                   'optika.tex',
                   2)
#     v = Variations([['A', 101, 102, '\\newpage'], ['B', 103, 104]],
#                    'valszam.tex',
#                    2)
    print("1"*50)
    print(v.one(1))
    framed = frame(v.one(0))
    file = open('temp.tex', "w")
    file.writelines(framed)
    file.close()
    print('I wrote file "temp.tex".')


def general_frame(text,
                  class_type='article',
                  class_argument="",
                  preamble_text=None
                  ):

    r""" Returns with the text in a LaTeX frame (preamble, \begin{document} etc)
    text can be a string or a list of strings (lines of the file),
    preamble_text must be list."""

    whole_text = ["\\documentclass%s{%s}\n" % (class_argument, class_type)]
    whole_text.append('\n')

    if isinstance(preamble_text, str):
        preamble_text = [preamble_text]
    if preamble_text:
        whole_text.extend(preamble_text)

    whole_text.append("\\begin{document}\n")
    whole_text.append('\n')
    whole_text.extend(text)
    whole_text.append('\n')
    whole_text.append("\n\\end{document}\n")
    return whole_text


def _general_frame_test():
    text = ['Itt van valami szöveg.\n', 'Ez a második sora.\n']
    framed = general_frame(text,
                           class_argument="[a4paper, 11pt]",
                           preamble_file='magyarpreambulum'
                           )
    file = open('temp.tex', "w")
    file.writelines(framed)
    file.close()
    print('I wrote file "temp.tex".')


def _VarExercise_test():
    code = 5
    text = """
Ha egy \interval[cm]{}{f=10..40} fókusztávolságú lencse elé
\interval[cm]{}{t=50..100} távolságra helyezek el egy \interval[cm]{}{T=2..6}
nagyságú tárgyat, akkor a \compute[cm]{K=T*(k/t)} nagyságú kép
\compute[cm]{k=1/(1/f-1/t)} távolságra keletkezik a lencsétől.
"""
    var = VarExercise(text, code, num=3, verbose=3)
    print(var)
    print(var.latex_plain(2))


class VarExercise:
    """ Makes, stores the values of a variation of an exercise.
    If there is some uncomputable formula, it returns with 1, else with 0.

    vartext(num) can make a variation for the text according the num-th
        variation.

    __str__() returns with the variations in a simple table.
    """

    def __init__(self, text, code, num=None, verbose=0):
        if verbose > 0:
            print("** ve  VarExercise.__init__ is running.")
        self.list = []  # Stores (values, erased_elements) pairs

        # The variable list is in the order, you want to see in the tables
        self.variable_list = []
        self.unit_list = []   # In the order of variable_list.
        self.sorted_variable_list = []
        self.formulas = []
        self.protected_variables = []  # It is not allowed to omit
        # these variables. Protected with "!" in \interval
        # control sequence.

        # if not text:
        #     raise ValueError("No text for code %d." % code)
        self.text = text
        self.code = code
        self.num = num
        self.verbose = verbose

        self.const_list = []
        self.interval_list = []
        self.compute_list = []
        self.ecChoose_list = []

        # Patterns
        self.intervalp = re.compile(r"""\\interval\s*
        ###Optional argument
          (\[\s*
             (?P<unit>[^\]]*)
             \s*
          ]\s*)?
            \s*
        ### Obligatory parameter
          {\s* (?P<base_value>[^}]*
                        ( | {[-+0-9]*} [^}]*)  # If there is e.g. 10^{-23}
                ) \s*}
            \s*
        ### Obligatory parameter
          {\s*
             (?P<obligatory>!)?
             (
                 (?P<name>[^\}]*)  \s*
                 = \s*
             )?
             (?P<interval>[^}]*)
          \s*}
          """, re.VERBOSE)

        # For testing, whether there is a \interval with an error
        self.intervalp0 = re.compile(r"\\interval")

        self.computep = re.compile(r"""\\compute\s*
          (\[\s*                   #Optional argument
             (?P<unit>[^\]]*)
             \s*
          ]\s*)?
             \s*
          {                   #Obligatory parameter
           \s*
             (?P<obligatory>!)?
             (?P<formula>
               (?P<name>\w*)
                \s*
                =
                \s*
               (?P<right>[^}]*)
             )
            \s*
           }
          """, re.VERBOSE)

        self.computep0 = re.compile(r"\\compute")

        self.constp = re.compile(r"""\\const\s*
          {                      #Obligatory parameter
           \s*
             (?P<name>[^}]*)
           \s*
           =
           \s*
            (?P<value>[^}]*)
           \s*
          }
          """, re.VERBOSE)

        self.constp0 = re.compile(r"\\const")

        self.ecChoosep = re.compile(r"""\\ecChoose\s*
        ###Optional argument
          (\[\s*
             (?P<unit>[^\]]*)
             \s*
          ]\s*)?
            \s*
        ### Obligatory parameter
          {\s* (?P<base_value>[^}]*
                ) \s*}
            \s*
        ### Obligatory parameter
          {\s*
                 (?P<name>[^\}]*)
          \s*}
          """, re.VERBOSE)

        # For testing, whether there is a \ecChoose with an error
        self.ecChoosep0 = re.compile(r"\\ecChoose")

        self.find_control_words()
        if not self.is_interval() and not self.is_ecChoose():
            return
        if self.verbose > 1:
            print("**ve interval_list=%s,\n**ve compute_list=%s,\n**ve ecChoose_list=%s" % \
               (self.interval_list, self.compute_list, ecChoose_list))
        self.uncomputable = 0
        if num:
            if self.is_interval():
                self.variations()
            else:
                self.choose_values()

    def find_control_words(self):
        """ It searches for control words, and append them to the matching
        list and their names to the self.variable_list if it is empty."""

        if self.verbose > 0:
            print('**cw varexercise.find_control_words() is running')

        row_number = 0
        for row in self.text:
            row_number += 1
            if self.verbose > 1:
                print('\ncw ***** Row %d: "%s"' % (row_number, row[:-1]))
            row = delete_remark(row)

            element_types = {
                "interval": dict(
                    regexp0=self.intervalp0,
                    regexp=self.intervalp,
                    keys=["name", "interval",
                          "base_value", "unit", "obligatory"],
                    element_list=self.interval_list,
                ),
                "compute": dict(
                    regexp0=self.computep0,
                    regexp=self.computep,
                    keys=["formula", "name", "right", "unit", "obligatory"],
                    element_list=self.compute_list,
                ),
                "const": dict(
                    regexp0=self.constp0,
                    regexp=self.constp,
                    keys=["name", "value"],
                    element_list=self.const_list,
                ),
                "ecChoose": dict(
                    regexp0=self.ecChoosep0,
                    regexp=self.ecChoosep,
                    keys=["name", "base_value", "unit"],
                    element_list=self.ecChoose_list,
                ),
            }
            for element_name in element_types:
                kwargs = element_types[element_name]
                kwargs["element_name"] = element_name
                self.search_for_element(row, row_number, **kwargs)

        for const in self.const_list:
            const['value'] = float(const['value'])
        self.make_variable_list()
        if self.is_interval():
            self.variaton_type = "interval"
            self.make_formulas()
        elif self.is_ecChoose():
            self.variaton_type = "ecChoose"

    def is_interval(self):
        """Returns with the logical value of 'there is interval(s) in the
        exercise'."""
        return len(self.interval_list) > 0

    def search_for_element(self, row, row_number,
                           regexp0, regexp, keys,
                           element_list, element_name):
        rest = row[:]
        shift = 0

        while True:
            result0 = regexp0.search(rest)
            if not result0:
                break
            result = regexp.search(rest)
            if (not result) or (result.start() != result0.start()):
                raise LaTeXError(element_name, self.code, row)

            if "obligatory" in keys and result.group('obligatory'):
                keys.remove("obligatory")
                self.protected_variables.append(result.group('name'))

            element = {}
            for key in keys:
                element[key] = result.group(key)
            element['row'] = row_number
            element['start'] = result.start() + shift
            end = result.end()
            element['end'] = end + shift

            element_list.append(element)
            if self.verbose > 0:
                print('**cw {0}:\n {1}'.format(element_name, element))

            rest = rest[end:]
            shift += end

    def is_ecChoose(self):
        """Returns with the logical value of 'there is ecChoose(es) in the exercise'."""
        return len(self.ecChoose_list) > 0

    def make_variable_list(self):
        if not self.variable_list:
            for interval in (self.interval_list + self.compute_list
                             + self.ecChoose_list):
                if interval['name']:
                    self.variable_list.append(interval['name'])
                    self.unit_list.append(interval['unit'])
            self.sorted_variable_list = self.variable_list[:]
            self.sorted_variable_list.sort()
            if self.verbose > 0:
                print('**cw %s' % self.variable_list)

    def make_formulas(self):
        if not self.formulas:
            for compute in self.compute_list:
                self.formulas.append(compute['formula'])

        equations = possibilities.make_equations(self.formulas,
                                                 set(self.variable_list))
        self.possibilities = list(
            possibilities.possibilities(equations, self.variable_list,
                                        set(self.protected_variables)))
        shuffled_possibilities = self.possibilities[:]
        random.shuffle(shuffled_possibilities)
        self.possibilities_cycle = itertools.cycle(shuffled_possibilities)

    def variations(self):
        """Makes the variations."""
        for i in range(self.num):
            self.one_variation()

    def one_variation(self):
        """ Make one variation for the values of the exercise.

        Just in the case if the values comes from \\intervals an \\compute.
        Stores them in self.list.
        If there is some uncomputable formulas, it set self.computable = 1."""
        if self.verbose > 0:
            print('**ov VarExercise.one_variation() is running.')
        values = {}

        # Constants and functions
        # Mathematical constants
        # global pi
        e = math.e; pi = math.pi
        drad = 180/pi

        # See sind, cosd ... functions at the beginning of the file.
        # They work correctly?

        #Physical constants
        g = 9.81        # Gravitational acceleration [m/s^2]
        c = 3e8         # Speed of Light [m/s]
        h = 6.6262e-34  # Planck [Js]
        k = 1.38e-23    # Boltzmann [J/K]
        R = 8.31441     # k*NA [J/(mol*kg)]
        NA = 6.0225e23  # Avogadro [1/mol]
        gamma = 6.67e11 # Gravitational Constant [Nm^2/kg^2]
        qe= 1.60219e-19 # Elementary charge [C] (e is not free unfortunately)
        e0 = epsilon0 = 8.854187816e-12
                # Permittivity of Vacuum [As/(Vm)]
        mu0 = 4e-7*pi
                # Permeability of Vacuum [Vs/(Am)]
        K = 9e9         # 1/(4*pi*epsilon0)  [Vm/(As)]
        me = 9.1095e-31 # The mass of electron [kg]
        mu= 1.66056e-27 # Atomic mass unit [kg]
        sigma = 5.67e-8 # Stefan-Boltzmann Constant

        # For example there is a variable k, it is not equal to k (Planck const)
        for variable in self.variable_list:
            if self.verbose > 1:
                print('**ov %s = None' % variable)
            exec('%s = None' % variable)

        for const in self.const_list:
            exec('%(name)s = %(value)g' % const)
            if self.verbose > 1:
                print('**ov Let %(name)s = %(value)g' % const)

        for intv in self.interval_list:
            value, latex = interval_.random(intv['interval'])
            if intv['name']:
                name = intv['name']
                exec('%s = float(%g)' % (name, value))
                exec('values["%s"] = float(%g)' % (name, value))
        if self.verbose > 1:
            print('**ov values=float(%s)' % values)

        compute_list = self.compute_list[:]
        uncomputable = 0  # The number of the failed computation after
                          # a successful computation.

        while compute_list:
            compute = compute_list[0]
            if self.verbose > 1:
                print('**ov Formula: %s' % compute['formula'])
            try:
                exec(compute['formula'])
            except (NameError, TypeError):
                if self.verbose > 0:
                    print('**ov  Not %s is computable yet.' % compute['name'])

                compute_list.append(compute_list.pop(0))
                # It writes the first st the end

                uncomputable += 1
                if uncomputable == len(compute_list):
                    error('uncomputable', self.code)
                    self.uncomputable = 1
                    return
                continue
            except ValueError:
                print('Value Error. Formula is:')
                print(compute['formula'])
                return

            compute_list.pop(0)
            uncomputable = 0
            command = 'values["%(name)s"] = %(right)s' % compute
            if self.verbose > 2:
                print("**ov command: ", command)
            exec(command)
            if self.verbose > 2:
                print('**ov values are= %s' % values)

        possibilities = next(self.possibilities_cycle)
        erased_elements = set(self.variable_list) - possibilities
        if self.verbose > 1:
            print('**ov Values: %s' % values)
        if self.verbose > 0:
            print('**ov erased_elements: %s' % erased_elements)
        self.list.append((values, erased_elements))

    def vartext(self, num, full=0):
        """ It creates the text with the values of the num-th variation.

        If full = 0 it writes the values according erased_elements,
        else writes all the values.
        If there is no interval in the text, it returns with the base_text.

        """
        if self.verbose > 0:
            print('**vt varexercise.vartext() is running.')
        elif not self.is_interval() and not self.is_ecChoose():
            return self.text
        values, erased_elements = self.list[num]
        vtext = self.text[:]
        space = "\spacer"   # It is at the place of an erased element.

        element_list = (self.interval_list + self.compute_list
                        + self.ecChoose_list)
        for element in element_list:
            element['shift'] = 0

        for element in element_list:
            if self.verbose-1 > 0:
                print('vt Interval or compute: %s' % element)
            start = element['start'] + element['shift']
            end = element['end'] + element['shift']
            row = element['row']
            line = vtext[row - 1]
            if element['name']:
                value = values[element['name']]
            else:
                # It is just a transient solution
                value, latexstring = interval_.random(element['element'])
            ltx = latex_number(value)
            if element['unit']:
                ltx += '~' + element['unit']
            if element['name'] in erased_elements:
                ltx = space
            line = line[:start] +  \
                ltx +  \
                line[end:]
            vtext[row - 1] = line

            shift = len(ltx) - (end - start)
            for element2 in element_list:
                if row == element2['row'] and element2['start'] >= end:
                    element2['shift'] += shift
        return vtext

    def choose_values(self):
        """Choose random values for ecChoose."""
        ecTable = latex_tools.find_ecTable_in_exercise(self.text)
        values_from_ecTable = latex_tools.values_from_ecTable(ecTable)

        list_for_choose = values_from_ecTable["list_of_values"]
        variables = values_from_ecTable["variables"]

        random.shuffle(list_for_choose)
        cycle = itertools.cycle(list_for_choose)
        for j in range(self.num):
            choosen = next(cycle)
            values = {}

            for var, value in zip(variables, choosen):
                values[var] = value
            erased_elements = []
            self.list.append((values, erased_elements))

    def row(self, values, erased_elements=None):
        """Returns with one row of the ASCII table
        in a string."""

        str = ""
        erased_elements = erased_elements or []
        if self.verbose > 0:
            print("**row values=%s" % values)
        for var in self.variable_list:
            if self.is_ecChoose:
                str += "%9s  " % values[var]
            elif var in erased_elements:
                str += '%9.4g? ' % values[var]
            else:
                str += '%9.4g  ' % values[var]
        str += '\n'
        return str

    def string_unit(self, index):
        "Gives back the unit as an ASCII (non-LaTeX style) string."
        unit = self.unit_list[index]
        if not unit:
            return None
        from_to = (
            ('$', ''),
            ('\\', ''),
            ('^', ''),
            ('frac', ''),
            ('dfrac', ''),
            ('cdot', '.'),
        )
        for from_, to in from_to:
            unit = unit.replace(from_, to)
        return unit

    def __str__(self):
        "Prints the variations as an ASCII table."
        str = "\n    "
        for i in range(len(self.variable_list)):
            var = self.variable_list[i]
            str += '%9.10s  ' % var
        str += '\n'

        str += "    "
        for i in range(len(self.variable_list)):
            unit = self.string_unit(i)
            if unit:
                unit = "[%s]" % unit
                str += '%9.10s  ' % unit
            else:
                str += ' '*11
        str += '\n'

        var_num = 0
        for values, erased_elements in self.list:
            var_num += 1
            str += '%3d.' % var_num
            str += self.row(values, erased_elements)
        return str

    def append(self, values, erased_elements):
        self.list.append((values, erased_elements))

        # controls, that the variables in values are correct.
        variables = values.keys()
        variables.sort()
        if variables != self.sorted_variable_list:
            raise ValueError('bad variables in dictionary values')

    def latexrow(self, string_list):
        '''Returns with a latex row of values in table format.
        The erased elements are boldface.'''

        if not string_list:
            return ''
        return latextable_row(string_list)

    def latex_string_list(self,
                          values, erased_elements=[],
                          sizes=('large', 'small')):
        """Returns with list of the values of the variables in LaTeX format.

        The erased_elements are with question mark.

        """
        if not self.variable_list:
            return ''
        string_list = []
        large, small = sizes
        for var in self.variable_list:
            erased = var in erased_elements
            mark = '?' if erased else ' '
            string = '{value:>5}{mark}'.format(
                value=latex_number(values[var]), mark=mark)
            size = large if erased else small
            if size:
                string = '{{\\{size} {string}}}'.format(
                    string=string, size=size)
            string_list.append(string)
        return string_list

    def latex_plain(self, num):
        """Returns with a plain latex format of the n-th variation,
        as latexrow (not in table format)."""
        if self.verbose > 0:
            print("** lp latex_plain is running.")
        if self.verbose > 1:
            print("*lp num=%d\n   self.list=%s" % (num, self.list))
        if not self.list:
            return ""
        values, erased_elements = self.list[num - 1]
        string_list = self.latex_string_list(values, erased_elements)
        if not string_list:
            raise ValueError('There is not values for the variation')
            # return '-\;'

        for i in range(len(string_list)):
            unit = self.unit_list[i] or ''
            name = self.variable_list[i]
            value_string = string_list[i]
            string_list[i] = '%s = %s~%s' % (name, value_string, unit)

        str = ',\\hspace{10pt plus 1cm} '.join(string_list)
        str = str + ';\\\\'
        return str

    def latextable(self, sizes=('', '')):
        ''' It returns with the variations in a LaTeX table format.'''
        if not self.variable_list:
            return []
        rows = ['\n']
        str = "\\begin{{tabular}}{{*{{{}}}{{r}}}}\n  \\hline\n".format(
            len(self.variable_list))
        rows.append(str)

        vars = ' ' + '& '.join(
            ['{:>5} '.format(var) for var in self.variable_list])
        vars += '\\\\\n'
        rows.append(vars)

        for values, erased_elements in self.list:
            string_list = self.latex_string_list(values,
                                                 erased_elements, sizes=sizes)
            rows.append(self.latexrow(string_list))
        rows.append('  \\hline\n\\end{tabular}\n')

        return rows


def exercise_test(text, variation_number=5, verbose=1, with_latextable=0):
    if verbose:
        print()
        print_text(text)
        print()

    code_number = 1001  # Bluff
    ex = VarExercise(text, code_number, variation_number, verbose=verbose-1)

    print(*ex.text, sep='')
    print(ex)

    # TODO write a more compact program to print the values below

    print('variable list:', *sorted(ex.variable_list))
    print('interval list:')
    for i in ex.interval_list:
        print(' ', '{name}={interval}'.format(**i))
    print('compute list:')
    for i in ex.compute_list:
        print(' ', '{formula}'.format(**i))
    print('const list:')
    for i in ex.const_list:
        print(' ', '{name}={value}'.format(**i))
    print('protected_variables:')
    pv = ex.protected_variables
    if pv:
        print(' ', *ex.protected_variables)
    else:
        print('  None')

    if 'possibilities' in dir(ex):
        print('possibilities ({}):'.format(len(ex.possibilities)))
        possibilities = [' '.join(sorted(p)) for p in ex.possibilities]
        print(' ', '\n  '.join(possibilities))

    if ex.vartext(0):
        print('One variation:\n')
        print(*ex.vartext(0))

    else:
        print('Uncomputable formulas in the exercise.')
        return 'uncomputable'

    if with_latextable:
        print(*ex.latextable(), sep='')


def _exercise_test(code_number, file_name=None, variation_number=5,
                   verbose=1, with_latextable=0):
    if verbose:
        print('**et _exercise_test() running.')
    file = ExerciseBook(file_name, file_type='testpaper', verbose=verbose - 1)
    print("**et codes=%s" % file.code_list)
    text = file.exercise_text(code_number)
    if not text:
        error("exercise missing", code_number)
        return
    if verbose and text:
        print()
        print_text(text)
        print()

    ex = VarExercise(text, code_number, variation_number, verbose=1)

    if verbose:
        print("**et ex='%s'" % ex)

    if ex.vartext(0):
        for line in ex.vartext(0):
            print(line[:-1])
    else:
        print('Uncomputable formulas in the exercise.')
        return 'uncomputable'

    if with_latextable:
        for i in range(1, variation_number + 1):
            print(ex.latex_plain(i))


def latex_number(value, verbose=-1):
    """ It converts a value to LaTeX format."""

    if verbose > 0:
        print('# latex value   = "%s"' % value)
    if isinstance(value, str):
        return value
    vstring = '%.4g' % value
    if verbose > 0:
        print('# latex vstring = "%s"' % vstring)
    if vstring.find('e+0') > -1:
        vstring = vstring.replace('e+0', times + '10^{') + '}'
    elif vstring.find('e-0') > -1:
        vstring = vstring.replace('e-0', times + '10^{-') + '}'
    elif 'e' in vstring:
        vstring = vstring.replace('e', times + '10^{') + '}'
    if '.' in vstring and decimal_point != '.':
        vstring = vstring.replace('.', decimal_point)

    latex = vstring.replace('+', '')
    if "^" in latex:
        latex = '$%s$' % latex
    return latex


def delete_remark(string):
    ''' delete_remark(string)  ->  string2

    string2 is the string without a LaTeX remark
      (removes the remark from the end of the string
      it deletes \\-s too).

    '''
    remark0p = re.compile(r''' ^ (\\\\)*   %  .*  ''',  re.VERBOSE)
    string = remark0p.sub('', string)

    remarkp =re.compile(r'''
                   (?P<last>[^\\])  # the case % but not \%
                   (\\\\)*
                   %
                   .*
                   ''', re.VERBOSE)

    string = remarkp.sub('\g<last>', string)
    return string


def latextable_row(string_list):
    for str in string_list:
        row = ' &'.join(string_list)
    row += ' \\\\\n'
    return row


if __name__ == '__main__':
    # _exercise_test(48, 'elektromagnesseg.tex', verbose = 3)
    # _exercise_test(49, 'mechanika.tex', verbose = 3)
    # _exercise_test(22, 'szilardsagtan.tex', verbose = 2)
    # _exercise_test(404, 'hotan.tex', verbose = 2)
    # _delete_remark_test()
    # _frame_test()
    _general_frame_test()
    # _variation_test()
    # _testpaper_frame_test()
    # _latex_test()
    # _VarExercise_test()