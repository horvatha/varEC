# -*- coding: utf-8 -*-

"""
 BASE SETTINGS
 Ha változtatni akarsz, keresd meg a
##    VÁLTOZTATHATÓAK
 sort.  Az után szerepelnek a legfontosabb beállítások.

    For Hungarian Users
 Default values. Change it, if you want.
"""

GROUP = 'physics'		# I will use bin/physics.py

code_interval = (1, 10000)

import time


# If you give here the paths, you need only type the
# filename in interactiv mode.
file_paths = ['.', 'physics_en']

# Standard group names / Szokásos csoportnevek
group_names = 'ABCDEFGHIJKLMNOPQRSTUVZ'

# Language (according to babel)/ Nyelv
# It can be 'magyar' only at this time.
# Perhaps it will be 'english', 'german', 'ngerman' ...
babel_lang = 'magyar'

# It will be at %s in r"\documentclass%s{article}"
page = 'letter'
fontsize = 11

exercise_numbers = []  # It is just for preventing Syntax Warning
# Next line usually imports:
# input_files, exercise_numbers, date, inst, title, course, num
# It may import class_argument and babel_lang too.
exec('from .%s import *' % GROUP)
if isinstance(input_files, str):
    input_files = input_files.split()


# Preambulum in Hungarian language.
# Preambulum a magyar nyelvhez.
preamble_languages = r"""
"""

# Packages & Environments
preamble_text_base = plus = r"""
%% Ha mégis KELL MEGOLDÁS, a következő sorban a "testpaper"
%% szót írd át "plain"-re
\newcommand{\doctype}{testpaper}

\input{magyarpreambulum}
\input{formats}

%% Itt esetleg állíthatod a többi logikai változót. (def_hu.tex)

\input{commands_hu}

%%%% FEJ és LáBLéC
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{fancyhdr}
\pagestyle{fancy}
\lhead{%s}
\rhead{%s}
\lfoot{%s}
\rfoot{%s}
\cfoot{}

%% Ide jöhetnek a különböző csomagok (\usepackage{ })
"""

# For intervalrandom() in interval.py
times = '\\times'
decimal_point = '.'


from varEC.datalist import DataList


files = DataList('Files')
files.append(
    'input',
    'The names of the exercise-serieses wich contains the exercises',
    input_files
)
files.append('output', 'The whole name of the output file', output_file)


header_footer = DataList('Dates for header and footer')
header_footer.append('title', 'Title', 'Physics')
header_footer.append('inst', 'Institution', 'XY TeXnical Scool')
header_footer.append('course', 'Course, grade', 'LaTeX (correspondence course)')
shift = 1  # Egy nap múlva (holnap)
localtime = time.localtime(time.time() + shift*24*3600)
date_en = time.strftime("%d %m %Y", localtime)  # English format
try:
    date = date
except NameError:
    date = date_en

header_footer.append('date', 'Date', date)

make = DataList('The format you need')
try:
    format = format
except NameError:
    format = 0
make.append(
    'format',
    'The file format you need (it can be 0, dvi, ps, pdf, pdflatex)',
    format
)

variations = DataList('Variations')
try:
    num = num
except NameError:
    num = -1  # Not valid value. It will ask it, if there is no value.
variations.append('num', 'The number of variations', num)
