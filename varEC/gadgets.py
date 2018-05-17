# -*- coding: utf-8 -*-

import locale
import time
import datetime

month_name = ['', 'január', 'február', 'március', 'április',
              'május', 'június', 'július', 'augusztus',
              'szeptember', 'október',  'november', 'december']
month_length = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_locale_month_name(month_num, locale_name=''):
    locale.setlocale(locale.LC_ALL, locale_name)
    return locale.nl_langinfo(locale.MON_1-1+month_num)


def date_string(string, with_weekday=True):
    """Egy 040312 kezdetű fájlból a "2004. március 12." sztringet hozza létre.
    Tipikus használata:
    date=date_string(output_file)
    """
    assert string[:6].isdigit()
    year, month, day = string[:2], int(string[2:4]), int(string[4:6])
    assert is_date_valid(year, month, day), "must be a valid date"
    date_string = date_string_from_triple(year, month, day)
    if with_weekday:
        weekday_part = " ({})".format(get_weekday(2000+int(year), month, day))
    else:
        weekday_part = ""
    return date_string + weekday_part


def tomorrow_triple():
    shift = 1
    lt = time.localtime(time.time() + shift*24*3600)
    return lt.tm_year, lt.tm_mon, lt.tm_mday

weekdays = "hétfő kedd szerda csütörtök péntek szombat vasárnap".split()
def get_weekday(year, month, day):
    dt = datetime.datetime(year, month, day)
    return weekdays[dt.weekday()]


def is_date_valid(year, month, day):
    return month < 13 and 0 < day <= month_length[month]


def date_string_from_triple(year, month, day):
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

newpage = r"\ifthenelse  {\equal{\doctype}{testpaper}}{\newpage}{}"


def textin(text, type_="testpaper", elsetext=""):
    assert type_ in {"testpaper", "plain", "draft"}
    return r"\ifthenelse {\equal{\doctype}{%s}} {%s} {%s}" % \
        (type_, text, elsetext)
