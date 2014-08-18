# -*- coding: utf-8 -*-

import locale

month_name = ['', 'január', 'február', 'március', 'április',
              'május', 'június', 'július', 'augusztus',
              'szeptember', 'október',  'november', 'december']
month_length = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_locale_month_name(month_num, locale_name=''):
    locale.setlocale(locale.LC_ALL, locale_name)
    return locale.nl_langinfo(locale.MON_1-1+month_num)


def date_string(string):
    """Egy 040312 kezdetű fájlból a "2004. március 12." sztringet hozza létre.
Tipikus használata:
date=date_string(output_file)
    """
    assert string[:6].isdigit()
    year, month, day = string[:2], int(string[2:4]), int(string[4:6])
    assert month < 13
    assert 0 < day <= month_length[month]
    return '20%s. %s %d.' % (year, month_name[month], day)


TABLE_TEMPLATE = r'''\begin{tabular}[b]{%s}
\hline
%s
\hline
%s
\hline
%s
\hline
\end{tabular}
'''


def table(*scores, **kwargs):
    def line(*list):
        str = "%s" % list[0]
        for item in list[1:]:
            str = str + '&\t' + "%s" % item
        str = str + r'\\'
        return str

    start = kwargs.pop("start", 1)
    assert not kwargs
    item_number = len(scores)
    num = ["%d." % n for n in range(start, start+item_number)] + ["Össz."]
    scores += (sum(scores),)
    table = TABLE_TEMPLATE % ('|'+'r|'*(item_number+1), line(*num),
                              "&\t"*item_number + r'\\', line(*scores))
    return table


vfill = r"\ifthenelse  {\equal{\doctype}{testpaper}}{\vfill}{}"


def textin(text, type_="testpaper", elsetext=""):
    assert type_ in {"testpaper", "plain", "draft"}
    return r"\ifthenelse {\equal{\doctype}{%s}} {%s} {%s}" % \
        (type_, text, elsetext)
