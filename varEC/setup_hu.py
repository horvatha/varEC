# -*- coding: utf-8 -*-

"""
 ALAPBEÁLLÍTÁSOK.
 Ha változtatni akarsz, keresd meg a
##    VÁLTOZTATHATÓAK
 sort.  Az után szerepelnek a legfontosabb beállítások.

    This file is for Hungarian users
 Default values. Change it, if you want.
"""

#en[3] GROUP='physics'      # I will use bin/physics.py
FILE_GROUP='villanytan'  # I will use bin/villanytan.py
FILE_GROUP='villamos_energetika'
FILE_GROUP='halozatok'
FILE_GROUP='informatika'     # I will use bin/informatika.py
FILE_GROUP='szamtudmat'      # I will use bin/szamtudmat.py
FILE_GROUP='hiradastechnika'     # I will use bin/hiradastechnika.py
FILE_GROUP='mat'     # I will use bin/mat.py
FILE_GROUP='fizika'      # I will use bin/fizika.py

code_interval = (1,10000)

##  It will be perhaps in an another file:
##  'fesor_config.py'


import time

# If you give here the paths, you need only type the
# filename in interactiv mode.
#en file_paths = ['base','.','physics_en']
file_paths = ['base', '.', 'matematika_hu', 'fizika_hu', 'physics_en',
        'szamtudmat', 'hiradastechnika', 'informatika', 'halozatok',
        'villamos_energetika',
        ]

# Standard group names / Szokásos csoportnevek
group_names='ABCDEFGHIJKLMNOPQRSTUVZ'

# Language (according to babel)/ Nyelv
# It can be 'magyar' only at this time.
# Perhaps it will be 'english', 'german', 'ngerman' ...
babel_lang='magyar'

# It will be at %s in r"\documentclass%s{article}"
#en page = 'letter'
page = 'a4paper'
fontsize = 11

exercise_numbers = []  # It is just for preventing Syntax Warning
# Next line usually imports:
# input_files, exercise_numbers, date, inst, title, course, num
# It may import class_argument and babel_lang too.
exec('from .%s import *' % FILE_GROUP)
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

## For intervalrandom() in interval.py
#en times = '\\times'
times = '\cdot'
#en decimal_point='.'
decimal_point=','


from varEC.datalist import DataList


#en files = DataList('Files')
files = DataList('Fájlok')
#en files.append('input', 'The names of the exercise-serieses wich contains the exercises', input_files)
files.append('input', 'A feladatokat tartalmazó fájlok nevei', input_files)
#en files.append('output', 'The whole name of the output file', output_file)
files.append('output', 'A kimeneti fájl teljes neve', output_file)


#en header_footer = DataList('Dates for header and footer')
header_footer = DataList('A fej- és láblécbe kerülő adatok')
#en header_footer.append('title', 'Title','Physics')  #Matematika dolgozat')
header_footer.append('title', 'Cím',title)
#en header_footer.append('inst', 'Institution', 'XY TeXnical Scool')
header_footer.append('inst', 'Az intézet neve', inst)
#en header_footer.append('course','Course, grade','LaTeX (correspondence course)') #Villamosmérnök (nappali)')
header_footer.append('course','Tagozat, szak, évfolyam',course)
shift = 1  # Egy nap múlva (holnap)
localtime = time.localtime(time.time() + shift*24*3600)
#en[7] date_en = time.strftime("%d %m %Y", localtime) # English format
date_hu = time.strftime("%Y.  %d.", localtime).lower()
month_name = ['', 'január', 'február', 'március', 'április',
              'május', 'június', 'július', 'augusztus',
              'szeptember', 'október',  'november', 'december']
month = localtime[1]
date_hu = date_hu[:6] + month_name[month] + date_hu[6:]

try:
    date = date
except NameError:
#en    date = date_en
    date = date_hu

#en header_footer.append('date','Date', date)
header_footer.append('date','Dátum', date)

## other = DataList()
## other.set_text('Egyéb adatok és beállítások')
## other.append('newline', 'Hol legyen új sor?', )
## if __name__ == '__main__':
##     setup([header_footer,files])

#en make = DataList('The format you need')
make = DataList('A szükséges formátum')
try:
    format = format
except NameError:
    format = 0
#en make.append('format','The file format you need (it can be 0, dvi, ps, pdf, pdflatex)', format)
make.append('format','A számodra szükséges fájlformátum (lehet tex, dvi, ps, pdf, pdflatex)', format)

#en variations = DataList('Variations')
variations = DataList('Változatok')
try:
    num = num
except NameError:
    num = -1 # Not valid value. It will ask it, if there is no value.
#en variations.append('num', 'The number of variations', num)
variations.append('num', 'A szükséges változatok száma', num)
