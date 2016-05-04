# -*- coding: utf-8 -*-
#  -*- Python -*-

"""Számítástudomány matematikai alapjai (Diszkrét matematika) dolgozatpéldák."""

from varEC.gadgets import date_string
# Egy 040312 kezdetű fájlból a "2004. március 12." sztringet hozza létre.
# Tipikus használata:
# date = date_string(output_file)

from varEC.gadgets import table
# A table függvény elkészít egy latex ponttáblázatot.
# Ha a pontszámok 3,4,5,4,3, akkor table(3,4,5,4,3) értéket kell a feladatsorok
# közé szúrni.

from varEC.gadgets import vfill, newpage
# \vfill-t (rugalmas közt) rak be a feladatok közé. A megoldáshoz nem.

from varEC.gadgets import textin
# A textin függvény az alábbi alakban csak a plain-ben ír újsort.
# textin(r"\newpage", "plain")
# A második paraméter elhagyható, alapértelmezése "testpaper".

input_files = ["szamtudmat.tex"]

Greibach = 'Sheila Greibach'
Chomsky = 'Noam Chomsky'
Salomaa = 'Arto Salomaa'

#####################
output_file = '070125sztudmat_tav.tex'
course = 'Távoktatás'
inst = 'BMF SZGTI, Székesfehérvár'
title = 'Számítástudomány matematikai alapjai'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.5\textwidth}{
%%Név:\dotfill

Az itt elérhető 80 pont adódik hozzá a házi feladatokra kapott max. 20 ponthoz.
A feladatmegoldás ideje 60 perc.}
}
{}
""" % table(8, 6, 18, 20, 20, 8)
exercise_numbers = [
    ['A', eloszo, 5, vfill, 12, vfill, 17, vfill, 24, vfill,
     2, vfill, 19,
     # "\\newpage"
     ]
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
# Csak a dátumban más mint az előző!!!

output_file = '080114sztudmat_tav.tex'
course = 'Távoktatás'
inst = 'BMF ROIK, Székesfehérvár'
title = 'Számítástudomány matematikai alapjai'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.5\textwidth}{
%%Név:\dotfill

Az itt elérhető 80 pont adódik hozzá a házi feladatokra kapott max. 20 ponthoz.
A feladatmegoldás ideje 60 perc.}
}
{}
""" % table(8, 6, 18, 20, 20, 8)
exercise_numbers = [
    ['A', eloszo, 5, vfill, 12, vfill, 17, vfill, 24, vfill,
     2, vfill, 19,
     # "\\newpage"
     ]
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '101004progpar.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Prog. paradigmák és Számítástudomány'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlap hátulján is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(14, 5, 6, 5)
exercise_numbers = [
    ['A', eloszo, 27, vfill, 18, vfill, 15, vfill, 28, vfill,
     # "\\newpage"
     ],
    ['B', eloszo, 26, vfill, 19, vfill, 16, vfill, 29, vfill,
     # "\\newpage"
     ],
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '101122progpar.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Prog. paradigmák és Számítástudomány'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlap hátulján is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(8, 3, 3, 2, 8, 6)
exercise_numbers = [
    [Greibach, eloszo, 34, 40, vfill, 38, vfill,
     36, vfill, "\\newpage", 31, vfill, 42,
     vfill, "\\newpage"
     ],
    [Chomsky, eloszo, 35, 41, vfill, 39,
     vfill, 37, vfill, "\\newpage", 32, vfill, 30,
     vfill  # "\\newpage"
     ],
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '101206progpar_jav.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Prog. paradigmák és Számítástudomány'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlap hátulján is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
"""
exercise_numbers = [
    ['Alan Turing', eloszo % table(14, 5, 6, 5),
     27, vfill, 18, vfill, 15, vfill, 28, vfill,
     "\\newpage"
     ],
    [Chomsky,    eloszo % table(8, 2, 3, 3, 7, 7),
     44, 36, vfill, 39, vfill, 38, vfill, "\\newpage", 32, vfill, 43,
     vfill  # "\\newpage"
     ],
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '110418formalis_nyelvek.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlap hátulján is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(8, 4, 3, 2, 7, 6)
exercise_numbers = [
    [Greibach, eloszo, 34, 38, vfill, 40, vfill,
     36, vfill, "\\newpage", 31, vfill, 50,
     vfill, "\\newpage"
     ],
    [Chomsky, eloszo, 35, 49, vfill, 39,
     vfill, 37, vfill, "\\newpage", 32, vfill, 30,
     vfill  # "\\newpage"
     ],
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '111206progpar.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(18, 10, 10, 18, 14)
exercise_numbers = [
    [Greibach, eloszo, 27, vfill, 15, vfill,
     "\\newpage",  28, vfill, 32, vfill, 51,
     ],
    [Chomsky, eloszo, 26, vfill, 16, vfill,
     "\\newpage", 29, vfill, 33, vfill, 43, vfill,
     ],
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '111215progpar_jav.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(18, 10, 10, 18, 14)
exercise_numbers = [
    [Greibach, eloszo, 26, vfill, 15, vfill,
     "\\newpage",  28, vfill, 32, vfill, 43,
     ],
    [Chomsky, eloszo, 27, vfill, 16, vfill,
     "\\newpage", 52, vfill, 33, vfill, 51, vfill,
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '120322formalis_nyelvek.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 40 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlap hátulján is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(6, 5, 5, 4)
exercise_numbers = [
    [Chomsky, eloszo, 27, vfill, 53, vfill,
     "%%\\newpage", 52, vfill, 54, vfill,
     ],
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '120503formalis_nyelvek_2zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlap hátulján is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(7, 2, 7, 4)
exercise_numbers = [
    [Greibach, eloszo, 33, vfill, 55, vfill, 31, vfill, 46,
     vfill, "\\newpage"
     ],
    [Chomsky,    eloszo, 32, vfill, 56, vfill, 51,  vfill, 45,
     vfill  # "\\newpage"
     ],
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '121202progpar.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(15, 9, 7, 9, 8, 12)
exercise_numbers = [
    [Greibach, eloszo, 27, vfill, 18, vfill,
     "\\newpage",  59, 61, vfill, 39, vfill, 32,
     ],
    [Chomsky, eloszo, 26, vfill, 19, vfill,
     "\\newpage", 60, 28, vfill, 38, vfill, 43,
     ],
]
num = 0
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '121210progpar_jav.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}

{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(15, 9, 7, 9, 8, 12)
exercise_numbers = [
    [Greibach, eloszo, 26, vfill, 63, vfill,
     "\\newpage", 59, 62, vfill, 37, vfill, 43,
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '121221progpar_pot.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák pótzh'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(15, 9, 7, 9, 8, 12)
exercise_numbers = [
    ['John Backus', eloszo, 26, vfill, 63, vfill,
     "\\newpage",  59, 62, vfill, 37, vfill, 43,
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '130118progpar_vizsga.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapo is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(18, 10, 10, 18, 14)
exercise_numbers = [
    [Greibach, eloszo, 26, vfill, 15, vfill,
     "\\newpage",  28, vfill, 32, vfill, 43,
     ],
    [Chomsky, eloszo, 27, vfill, 16, vfill,
     "\\newpage", 52, vfill, 33, vfill, 51, vfill,
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '130313formalnyelv.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(3, 4, 4, 9)
exercise_numbers = [
    [Greibach, eloszo, 54, vfill, 28, vfill, vfill,
     19, vfill, vfill, "\\newpage", 26, "\\newpage",
     ],
    [Chomsky, eloszo, 54, vfill, 61, vfill, vfill,
     18, vfill, vfill, "\\newpage", 27, "\\newpage",
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '130507formalis_nyelvek_2zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.
A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon található név kívül legyen.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(8, 2, 7, 3)
exercise_numbers = [
    [Greibach, eloszo, 54, vfill, 28, vfill, vfill,
     19, vfill, vfill, "\\newpage", 26, "\\newpage",
     ],
    [Chomsky, eloszo, 32, vfill, 56, vfill, "\\newpage", 67,  vfill, 66,
     vfill  # "\\newpage"
     ],
]
num = 5
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '130610progpar_vizsga.tex'
course = 'Levelező, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapo is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(18, 10, 10, 18, 14)
exercise_numbers = [
    [Greibach, eloszo, 26, vfill, 15, vfill,
     "\\newpage",  28, vfill, 32, vfill, 43,
     ],
    [Chomsky, eloszo, 27, vfill, 16, vfill,
     "\\newpage", 52, vfill, 33, vfill, 51, vfill,
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '131205progpar.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 50 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(12, 7, 7, 6, 8)
exercise_numbers = [
    [Greibach, eloszo, 27, vfill, 18, vfill,
     "\\newpage",  61, vfill, 39, vfill, 68, vfill,
     ],
    [Chomsky, eloszo, 26, vfill, 19, vfill,
     "\\newpage", 28, vfill, 38, vfill, 43, vfill,
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '131211progpar_pot.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(14, 8, 8, 10)
exercise_numbers = [
    ['John Backus', eloszo, 69, vfill, 18, vfill,
     "\\newpage",  29, vfill, 43, vfill,
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
# a decemberi alapján készült
output_file = '140108progpar_pot.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(14, 8, 8, 10)
exercise_numbers = [
    ['John Backus', eloszo, 69, vfill, 18, vfill,
     "\\newpage",  29, vfill, 43, vfill,
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '140318formalnyelv_1zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek 1. zh'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(3, 4, 4, 9)
exercise_numbers = [
    [Greibach, eloszo, 54, vfill, 28, vfill, vfill,
     70, "\\newpage", 26, "\\newpage",
     ],
    [Chomsky, eloszo, 54, vfill, 61, vfill, vfill,
     71, "\\newpage", 27, "\\newpage",
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '140506formalis_nyelvek_2zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.
A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon található név kívül legyen.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(8, 2, 7, 3)
exercise_numbers = [
    [Greibach, eloszo, 73, vfill, 65, vfill, vfill, "\\newpage",
     64, vfill, vfill, 66, "\\newpage",
     ],
    [Chomsky, eloszo, 32, vfill, 56, vfill, "\\newpage", 67,  vfill, 66,
     vfill  # "\\newpage"
     ],
]
num = 5
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '140513formalis_nyelvek_jav_zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek javító ZH'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \hspace{.25\textwidth} \parbox[b]{.5\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.
A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon található név kívül legyen.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
"""
exercise_numbers = [
    ['1. zh', eloszo % table(3, 4, 4, 9), 54, vfill, 61, vfill, vfill,
     72, "\\newpage", 69, "\\newpage",
     ],
    ['2. zh',    eloszo % table(8, 2, 7, 3), 75, vfill, 56, vfill, "\\newpage",
     43, vfill, vfill, 66, vfill  # "\\newpage"
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '140520formalis_nyelvek_pot_zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek pótZH'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \hspace{.25\textwidth} \parbox[b]{.5\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.
A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon található név kívül legyen.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
"""
exercise_numbers = [
    ['1. zh', eloszo % table(3, 4, 4, 9), 54, vfill, 61, vfill, vfill,
     72, "\\newpage", 69, "\\newpage",
     ],
    ['2. zh', eloszo % table(8, 2, 7, 3), 75, vfill, 56, vfill, "\\newpage",
     43, vfill, vfill, 66, vfill
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '140526progpar_vizsga.tex'
course = 'Levelező, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon (hátoldalon is) dolgozhatnak.
%%Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(16, 8, 8, 10, 16, 12)
exercise_numbers = [
    [Greibach, eloszo, 69, vfill, 15, vfill, 59,
     "\\newpage",  28, vfill, 73, vfill, 43,
     ],
    [Chomsky, eloszo, 27, vfill, 16, vfill, 60,
     "\\newpage", 52, vfill, 75, vfill, 51, vfill,
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '140603progpar_vizsga_levelezo.tex'
course = 'Levelező, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.5\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon (hátoldalon is) dolgozhatnak.
Az utolsó pontszám a félévközi
tesztekhez tartozó pontszám arányosan csökkentve.
%%Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(10, 5, 5, 10, 10, 10, 7, 7, 16)
exercise_numbers = [
    [Greibach, eloszo, 69, vfill, 15, vfill,
     "\\newpage",  28, vfill, 73, vfill, 43,
     "\\newpage",  54, vfill, 37, vfill, 59,
     "\\newpage",
     ],
    [Chomsky, eloszo, 27, vfill, 16, vfill,
     "\\newpage", 52, vfill, 75, vfill, 51, vfill,
     "\\newpage",  54, vfill, 40, vfill, 60,
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '140617progpar_vizsga_levelezo.tex'
course = 'Levelező, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.5\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 60 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon (hátoldalon is) dolgozhatnak.
Az utolsó pontszám a félévközi
tesztekhez tartozó pontszám arányosan csökkentve.
%%Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(10, 5, 5, 10, 10, 10, 7, 7, 16)
exercise_numbers = [
    [Greibach, eloszo, 69, vfill, 15, vfill,
     "\\newpage",  28, vfill, 73, vfill, 43,
     "\\newpage",  54, vfill, 37, vfill, 59,
     "\\newpage",
     ],
    [Chomsky, eloszo, 27, vfill, 16, vfill,
     "\\newpage", 52, vfill, 75, vfill, 51, vfill,
     "\\newpage",  54, vfill, 40, vfill, 60,
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '140826formalis_nyelvek_mafiok.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AMK, Székesfehérvár'
title = 'Formális nyelvek és gépek pótzárthelyi'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \hspace{.25\textwidth} \parbox[b]{.5\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.
A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon található név kívül legyen.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
"""
exercise_numbers = [
    [Greibach, eloszo % table(3, 4, 4, 9),
     32,
     54,
     "\\newpage",
     43,
     26,
     ],
]
num = 2
page = 'a4'
format = 'pdflatex'

#####################
output_file = '141203progpar.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 50 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(14, 8, 8, 10)
exercise_numbers = [
    [Greibach, eloszo, 27, vfill, 70,  # vfill,
     "\\newpage",  61, vfill, 75,  # vfill,
     ],
    [Chomsky, eloszo, 26, vfill, 19, vfill,
     "\\newpage", 28, vfill, vfill, 43, vfill,
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
# Az első és a második feladat nagyon átfedésben van.
output_file = '141210progpar_jav.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse
    {\equal{\doctype}{testpaper}}

{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 50 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(8, 8, 6, 10, 8)
exercise_numbers = [
    [Salomaa, eloszo, 62, vfill, 52, vfill,
     54, "\\newpage", 43, vfill, 33,
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '150310formalnyelv_1zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AREK, Székesfehérvár'
title = 'Formális nyelvek és gépek 1. zh'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(3, 4, 4, 9)
exercise_numbers = [
    [Greibach, eloszo, 54, vfill, 28, vfill, vfill,
     70, "\\newpage", 26, "\\newpage",
     ],
    [Chomsky, eloszo, 54, vfill, 62, vfill, vfill,
     71, "\\newpage", 27, "\\newpage",
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '150504formalis_nyelvek_2zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AMK, Székesfehérvár'
title = 'Formális nyelvek és gépek, 2. zh.'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.
A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon található név kívül legyen.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(8, 2, 7, 3)
exercise_numbers = [
    [Greibach, eloszo, 73, vfill, 65, vfill, vfill, "\\newpage",
     64, vfill, vfill, 72, "\\newpage",
     ],
    [Chomsky, eloszo, 32, vfill, 56, vfill, "\\newpage",
     67,  vfill, vfill, 66, vfill  # "\\newpage"
     ],
]
num = 5
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '150512_formalis_nyelvek_jav_zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AMK, Székesfehérvár'
title = 'Formális nyelvek és gépek, 2. zh.'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.
A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon található név kívül legyen.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
"""
exercise_numbers = [
    ['2. zh', eloszo % table(7, 2, 7, 4),
     77, vfill, vfill, 66, vfill, "\\newpage",
     76, vfill, vfill, 78, "\\newpage",
     ],
    ['1. zh', eloszo % table(3, 4, 4, 9), 54, 61, vfill,
     28, vfill, vfill, "\\newpage", 69, "\\newpage",
     ],
]
num = 1
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '151202progpar.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AMK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 50 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(14, 8, 8, 10)
exercise_numbers = [
    [Greibach, eloszo, 27, vfill, 70,  # vfill,
     "\\newpage",  61, vfill, 75,  # vfill,
     ],
    [Chomsky, eloszo, 26, vfill, 18, vfill,
     "\\newpage", 28, vfill, vfill, 43, vfill,
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '151209progpar_jav.tex'
course = 'Nappali, Villamosmérnök'
inst = 'ÓE AMK, Székesfehérvár'
title = 'Programozási paradigmák'
date = date_string(output_file)
eloszo = r"""
\ifthenelse
    {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 50 perc.

%%A feladatmegoldáshoz tollat használjanak!
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(5, 4, 3, 4, 4)
exercise_numbers = [
    [Salomaa, eloszo, 69, vfill, 52, vfill,
     54, newpage, 43, vfill, vfill, 32, vfill,  # 33,
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '160331formalnyelv_1zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AMK, Székesfehérvár'
title = 'Formális nyelvek és gépek 1. zh'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.7\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.

A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon is dolgozhatnak.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(3, 4, 4, 9)
exercise_numbers = [
    [Greibach, eloszo, 54, vfill, 28, vfill, vfill,
     70, "\\newpage", 69, "\\newpage",
     ],
    [Chomsky, eloszo, 54, vfill, 62, vfill, vfill,
     71, "\\newpage", 69, "\\newpage",
     ],
]
num = 2
page = '4a5'
page = 'a4'
format = 'pdflatex'

#####################
output_file = '160505formalis_nyelvek_2zh.tex'
course = 'Nappali, Mérnök informatikus'
inst = 'ÓE AMK, Székesfehérvár'
title = 'Formális nyelvek és gépek, 2. zh.'
date = date_string(output_file)
eloszo = r"""
\ifthenelse  {\equal{\doctype}{testpaper}}
{\noindent %s \:\parbox[b]{.6\textwidth}{
Név:\dotfill

A feladatmegoldás ideje 45 perc.
A feladatlapokat kérem vissza,
belehajtogatva az esetleg használt további lapokat.
A feladatlapon található név kívül legyen.
Íróeszközön kívül más segédeszköz nem használható.
}
}
{}
""" % table(8, 2, 7, 3)
exercise_numbers = [
    [Greibach, eloszo, 73, vfill, 65, vfill, vfill, "\\newpage",
     64, vfill, vfill, 66, vfill, "\\newpage",
     ],
    [Chomsky, eloszo, 32, vfill, 56, vfill, "\\newpage",
     67,  vfill, vfill, 66, vfill  # "\\newpage"
     ],
]
num = 5
page = '4a5'
page = 'a4'
format = 'pdflatex'
