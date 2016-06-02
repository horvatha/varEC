#!/usr/bin/env python3
#  -*- Python -*-
r"""
usage: ec-sorter.py [option]... [file]
See the manual (it's only in Hungarian): manual/index.html

                Options:

 Modes:
             --help, -h           Prints this text.
             --verbosity=NUM      The program will be more or less verbose.
                                  NUM can be -1, 0, 1, 2.
                                  Normally it is 0.
                                  1 and 2 are more verbose (for debugging).
                                  -1 writes hardly anything,
                                  it is used with automatic mode.
             --verbose, -v        The programm will be more verbose.
                                  Same as --verbosity=1
 Files:
             --group=FILE_GROUP   The given data will be searched
                                  in the bin/FILE_GROUP.py file.
                                  (Does not work yet.)

 Fileformats:
             --format=TYPE        Translates into TYPE.
                                  If TYPE is dvi, ps or pdf it translates
                                  with latex, dvips and ps2pdf.
                                  If TYPE is pdflatex it translates
                                  with pdflatex.
             --html               Translates into html with latex2html.
                                  (Doesn't work yet.)
 Others:
             --var=NUM            How many testpaper variations
                                  do you wants?
                                  (Perhaps it works.)

#############################################################

 Actual information:
    http://www.amk.uni-obuda.hu/harp/latex/ec

 It's a Python program. It makes exercise-series.
 It works on LaTeX exercise-serieses.  It selects exercises
 for a testpaper and make variations for it, if it is possible.

 There is Python in the most (if not all) of the Linux distributions.
 For Windows, Macintosh etc. see: www.python.org

 The format you need in the exercise-series or in the testpaper:

 \begin{exercise}{<exercise_code>}
 <The_text_of_the_exercise>
 \begin{solution}
 <The_text_of_the_solution>
 \end{solution}
 \end{exercise}

 For example:

 \begin{exercise}{912}
 Solve this equation.
 \[x^2 + 2x + 1 = 0\]
 \begin{solution}
   $ x_1 = x_2 = -1 $
 \end{solution}
 \end{exercise}

  Horváth Árpád 2002. Jul
  horvath.arpad@amk.uni-obuda.hu

"""
from __future__ import print_function

# Hungarian help
hu_help = \
    r"""
Használat: ec-sorter.py [opció]... [fájl]
Nézd meg a bővebb leírást: manual/index.html

opciók:

Módok:
        --4a5             A5-ös formátumot csinál,
                        és négyesével egy A4-es papírra helyezi.
                        (Papírtakarékos.
                        Ha egy csoport két a5-ös oldalra elfér,
                        akkor kettévágva a lapot egy hallgató
                        duplaoldalas a5-ös lapot kap.)
                        (Még nem működik.)
        --help, -h, -H       Segítséget ad.
        --verbosity=NUM      Bőbeszédűbb vagy kevésszavúbb lesz a program.
                        Jelenleg NUM lehet -1, 0, 1, 2.
                        Normál esetben 0.
                        1 és 2 egyre bőbeszédűbb (hibajavításhoz).
                        -1 kevés dolgot ír ki,
                        az automatikus módban használom.
        --verbose, -v     Bőbeszédűbb lesz a program.
                        ugyanaz mint --verbosity=1
Fájlok:
        --group=CSOPORT      A használt csoport neve. A beállításokat
                        a bin/CSOPORT.py fájlban keresi.
                        (Még nem működik.)

Fájlformátumok:  (Még nem mind működik.)
        --format=TÍPUS    Translates into TÍPUS.
                        Ha a TÍPUS dvi, ps vagy pdf
                        latex, dvips and ps2pdf programokkal
                        fordít.
                        Ha a TÍPUS pdflatex pdflatex-hel fordít.
        --html            HTML-be fordít latex2html-el.
                        (Még nem működik.)
        --print=MÓD       Nyomtat. MÓD: dvilj, dvilj4...
                        (Még nem működik.)
Egyéb:
        --var             Hányféle tesztlap variációt csináljon?
                        (Még nem működik.)

############################################################

Actual information:
Friss információk:
    http://www.amk.uni-obuda.hu/harp/latex/ec

It's a Python program. It makes exercise-series.
There is Python in the most of linux CD-s.
For windows, macintosh etc. see: www.python.org

Feladatsor feldolgozó program. LaTeX-ben írt dokumentumokat
dolgoz fel.  Egy feladatgyűjteményből válogat pl. egy dolgozathoz
feladatokat.

A szükséges formátum ilyen feladatok egymásutánja:

\begin{feladat}{<feladat_sorszám>}
<A_feladat_szövege>
\begin{megoldas}
<A_megoldás_szövege>
\end{megoldas}
\end{feladat}

Például:

\begin{feladat}{912}
Határozza meg a megoldását!
\[x^2 + 2x + 1 = 0\]
\begin{megoldas}
$ x_1 = x_2 = -1 $
\end{megoldas}
\end{feladat}

Horváth Árpád 2002 -- 2015
horvath.arpad@amk.uni-obuda.hu

"""

import sys
assert sys.version_info.major == 3, "varEC works with Python version 3"

from varEC import integerlist
from .common import BadCodeException, CodeNotFoundError
from .common import _

import os
import getopt

from varEC import varexercise

from varEC.lang import lang
try:
    exec('from varEC.setup_%s import *' % lang)
except ImportError:
    print("fesor: There's no setup_%s, I use setup_en" % lang)
    from varEC.setup_en import *


from varEC.message import message

from varEC.books import BookShelf

##########################################
#  Options
##########################################


class Options:
    verbose = 0
    help = 0
    variation = 0
    view = None

    def parse(self, args0):
        opts, args = getopt.getopt(args0,
                                   "avhHo:p:",
                                   ["verbose", "verbosity=",
                                    "help", "output=",
                                    "format=", "view=",
                                    "var=", "print="])

        for opt, arg in opts:
            # Modes
            if opt in ['-v', '--verbose']:
                self.verbose = 1
            elif opt == '--verbosity':
                self.verbose = int(arg)
            elif opt in ['-h', '-H', '--help']:
                self.help = 1
            # Things to do
            elif opt in ['--view']:
                self.view = arg
            elif opt == '--format':
                make.format = arg

            # Files
            elif opt in ["--var"]:
                variations.num = int(arg)
            elif opt in ["-o", "--output"]:
                if not os.path.splitext(arg)[1]:
                    arg = arg + ".tex"
                files.output = arg
            # elif opt == "--group":    # Does not work yet.
            #                           # It uses the group in setup_%s.py.
            #     settings = 'bin/%s.py' % arg
            #     if os.path.isfile(arg):
            #         files.group = arg
            #     else:
            #         raise getopt.GetoptError('"%s" is not a valid filename'
            #                                  % arg)
            elif opt in ['-p', "--print"]:
                pass
        return args


#  Functions for write exercises
###########################

def test_exercise_numbers():
    """ It writes the intervals and the not uniq numbers. """

    int_codelist = [x for x in books.codelist if isinstance(x, int)]

    message(_('1. The next files are in this group:'))
    for file in files.input:
        print("\t%s" % file)

    message(_('\n2. Intervals of exercise codes'
                  '(pl. 12..14 means: 12, 13, 14):'))
    integerlist.print_intervals(int_codelist)

    message(_('\n3. Not uniq exercise codes I found:'))
    num = integerlist.print_not_uniq(
        int_codelist,
        _('%d times is the code %d!'))
    if num == 0:
        message(_('None.'))

    # If there are bad arguments (which is not integer)
    # writes them.
    message(_('\n4. Bad arguments:'))
    bad_list = books.exercises_with_bad_arguments()
    if len(bad_list) > 0:
        for file_name, row, code in bad_list:
            raise BadCodeException(file_name, row, code)
    else:
        message(_('None.'))
    print()


#  Miscellaneous functions
###########################


def translate(file):
    """It makes the given translations.
    Returns with the names of the generated files.
    """

    change_format_4a5 = _('I changed the format '
                          'to %s because of the pagestyles 4a5!')
    new_files = []
    filename = file.name
    file0 = os.path.splitext(filename)[0]
    if page == '4a5':
        if make.format == 'pdflatex':
            make.format = "pdf"
            message(change_format_4a5 % "pdf")
        if make.format == 'dvi':
            make.format = "ps"
            message(change_format_4a5 % "ps")
    if make.format in ['dvi', 'ps', 'pdf']:
        os.system('latex %s' % filename)
        new_files.append("%s.dvi" % file0)
    if make.format in ['ps', 'pdf']:
        os.system('dvips %s.dvi -o' % file0)
        new_files.append("%s.ps" % file0)
    if make.format in ['pdflatex']:
        os.system('pdflatex %s' % filename)
        new_files.append("%s.pdf" % file0)
    if page == '4a5' and file.is_4a5:
        os.system('./4a5  %s.ps' % file0)
        new_files.append("%s_4a5.ps" % file0)
        os.system('rm  %s.ps' % file0)
        new_files.remove("%s.ps" % file0)
    if make.format == 'pdf':
        if page == '4a5' and file.is_4a5:
            os.system('ps2pdf %s_4a5.ps' % file0)
            new_files.append("%s_4a5.pdf" % file0)
        else:
            os.system('ps2pdf %s.ps' % file0)
            new_files.append("%s.pdf" % file0)
    return new_files


def get_ordered_codes(exercise_numbers):
    """Returns with the ordered codes in the exercise_numbers."""
    codes = []
    for group in exercise_numbers:
        for item in group:
            try:
                i = int(item)
                codes.append(i)
            except ValueError:
                pass
    codes.sort()
    codes = integerlist.uniq(codes)
    return codes

################################
#    Main program
################################


class OutputFile:
    def __init__(self, name, is_4a5=False):
        self.name = name
        self.is_4a5 = is_4a5


class OutputFiles:
    """Stores the files.

    is_4a5 is boolean: if it is True, it will translated  into 4a5 format.
    For non tex files it is meaningless.
    """
    def __init__(self):
        self.list = []

    def append(self, name, is_4a5=False):
        of = OutputFile(name, is_4a5)
        self.list.append(of)

    def extend(self, namelist):
        oflist = [OutputFile(name) for name in namelist]
        self.list.extend(oflist)

    def __str__(self):
        return ''.join(["\t\t%s\n" % file.name for file in self.list])


def get_pagesize(page):
    if page in ['4a5', 'a5']:
        pagesize = 'a5paper'
        solution_pagesize = 'a4paper'
    elif page == 'a4':
        pagesize = 'a4paper'
        solution_pagesize = 'a4paper'
    else:
        pagesize = page
        solution_pagesize = page
    list_pagesize = solution_pagesize
    return pagesize, solution_pagesize, list_pagesize


output_tex_files = OutputFiles()


def save_file(text, parameters, file_name, is_4a5=False):
    framed_text = varexercise.frame(
        text,
        **parameters
    )
    output_tex_files.append(file_name, is_4a5)
    if options.verbose > 0:
        message(_('I\'ve opened the file "%s".\n') % file_name)
    with open(file_name, 'w') as f:
        f.writelines(framed_text)


def make_testpapers(solution_file=True):

    books = BookShelf(files.input)

    codes = get_ordered_codes(exercise_numbers)
    number_of_variations = variations.num
    assert isinstance(number_of_variations, int) and number_of_variations >= 0

    global exercise_numbers
    try:
        variation = varexercise.Variations(
            exercise_numbers,
            files.input,
            number_of_variations
        )
    except CodeNotFoundError:
        message(_("Not all the exercise codes exists on the books "
                  "that was listed in the test paper."))
        return
    base_name, extension = os.path.splitext(files.output)

    pagesize, solution_pagesize, list_pagesize = get_pagesize(page)

    shared_parameters = dict(
        preamble_file="magyarpreambulum",
        rhead=header_footer.inst,
        lfoot=header_footer.course,
        rfoot=header_footer.date,
        definitions=books.definitions(codes)
    )

    solution_text = variation.one()
    text = solution_text if number_of_variations == 0 else variation.all()

    parameters = shared_parameters.copy()
    parameters.update(
        doc_type='testpaper',
        pagesize=pagesize,
        fontsize=fontsize,
        lhead=header_footer.title,
        cfoot=None,
    )
    file_name = "%s.tex" % base_name
    save_file(text, parameters, file_name, page == '4a5')

    if solution_file:

        parameters = shared_parameters.copy()
        parameters.update(
            doc_type='plain',
            pagesize=solution_pagesize,
            fontsize=fontsize,
            lhead=header_footer.title + " Megoldás",
            cfoot='\\thepage',
        )
        file_name = "%s_megold.tex" % base_name
        save_file(solution_text, parameters, file_name)

    if not number_of_variations == 0:
        text = variation.list()
        if not text:
            raise ValueError('no variations in TeX source.')
        else:
            parameters = shared_parameters.copy()
            parameters.update(
                doc_type='plain',
                fontsize=10,
                pagesize=list_pagesize,
                lhead=header_footer.title,
                cfoot='\\thepage',
            )
            file_name = "%s_list.tex" % base_name
            save_file(text, parameters, file_name)

    wrote_files_message = _('I wrote the files:\n %s\n')
    message(wrote_files_message % output_tex_files)

    other_output_files = OutputFiles()  # Non-tex files.
    if make.format == '0':
        make.format = 0
    if output_tex_files.list and make.format:
        message(_('I will translate the files. It will take a while.\n'))
        for file in output_tex_files.list:
            new_files = translate(file)
            other_output_files.extend(new_files)

    print('\n')
    message(wrote_files_message %
                ("%s%s" % (output_tex_files, other_output_files)))


def _make_testpapers_test():
    """ It tests varexercise.Variations."""
    print(files.input)
    global exercise_numbers
    number_of_variations = 1
    v = varexercise.Variations(
        exercise_numbers,
        files.input,
        number_of_variations
    )
    text = v.one(1)
    text = varexercise.frame(text)
    print(text)


def get_options():
    global options
    options = Options()
    options.parse(sys.argv[1:])


def main():
    """It is the main program."""
    if '-help' in sys.argv:
        print("Use --help, please.")
        return
    get_options()

    if options.help:
        if lang == 'hu':
            print(hu_help)
        else:
            print(__doc__)
        return

    message(_('''Have a good work. www.arek.uni-obuda.hu/harp/ec'''))

    make_testpapers()

