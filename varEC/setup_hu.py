# -*- coding: utf-8 -*-

from varEC import gadgets

"""
 ALAPBEÁLLÍTÁSOK.
 Ha változtatni akarsz, keresd meg a
##    VÁLTOZTATHATÓAK
 sort.  Az után szerepelnek a legfontosabb beállítások.

    This file is for Hungarian users
 Default values. Change it, if you want.
"""

# I will use varEC/{FILE_GROUP}.py as settings file.
FILE_GROUP = 'villanytan'
FILE_GROUP = 'halozatok'
FILE_GROUP = 'hiradastechnika'
FILE_GROUP = 'villamos_energetika'
FILE_GROUP = 'informatika'
FILE_GROUP = 'fizika'
FILE_GROUP = 'mat'
FILE_GROUP = 'szamtudmat'

code_interval = (1, 10000)

#  It will be perhaps in an another file:
#  'fesor_config.py'

# If you give here the paths, you need only type the
# filename in interactiv mode.
file_paths = ['base', '.', 'matematika_hu', 'fizika_hu', 'physics_en',
              'szamtudmat', 'hiradastechnika', 'informatika', 'halozatok',
              'villamos_energetika',
              ]

# Standard group names / Szokásos csoportnevek
group_names = 'ABCDEFGHIJKLMNOPQRSTUVZ'

# Language (according to babel)/ Nyelv
# It can be 'magyar' only at this time.
# Perhaps it will be 'english', 'german', 'ngerman' ...
babel_lang = 'magyar'

# It will be at %s in r"\documentclass%s{article}"
page = 'a4paper'
fontsize = 11

exercise_numbers = []  # It is just for preventing Syntax Warning
# Next line usually imports:
# input_files, exercise_numbers, date, inst, title, course, num
# It may import class_argument and babel_lang too.
exec('from .courses.%s import *' % FILE_GROUP)
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
times = r'\cdot'
decimal_point = ','


from varEC.datalist import DataList


files = DataList('Fájlok')
files.append('input', 'A feladatokat tartalmazó fájlok nevei', input_files)
files.append('output', 'A kimeneti fájl teljes neve', output_file)


header_footer = DataList('A fej- és láblécbe kerülő adatok')
header_footer.append('title', 'Cím', title)
header_footer.append('inst', 'Az intézet neve', inst)
header_footer.append('course', 'Tagozat,  szak,  évfolyam', course)

try:
    date = date
except NameError:
    date = gadgets.date_string_from_triple(gadgets.tomorrow_triple())

header_footer.append('date', 'Dátum', date)

make = DataList('A szükséges formátum')
try:
    format = format
except NameError:
    format = 0
make.append('format',
            'A számodra szükséges fájlformátum '
            '(lehet tex, dvi, ps, pdf, pdflatex)',
            format)

variations = DataList('Változatok')
try:
    num = num
except NameError:
    num = -1  # Not valid value. It will ask it, if there is no value.
variations.append('num', 'A szükséges változatok száma', num)
