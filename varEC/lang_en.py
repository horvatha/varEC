# -*- coding: utf-8 -*-
#  -*- Python -*-

##################################
#
#  Language section -- English
#
##################################
# 1. Environments and control sequences
env = {
    'exercise': 'exercise',
    'solution': 'solution',
    'group': 'exercisegroup'}

# 2. Asks
ask = {
    'group_numbers':'How many groups do you want? ',
    'group':'The name of group %s (Enter = "%s", "kk" = exit) ',
    'exercise':'The code of exercise %s? (Enter = end) ',
    'exercise code':'The code of exercise? ',
    'file name':'From which file? ',
    'file':'Which file search I from? ',
    'enter':'Push >Enter< to continue, or "q" to quit! ',
    'change': 'Do you want to change? (Enter = no, y or yes = yes)',
    'use exercise_numbers': 'Can I use it? (Enter = yes, n or no = no )',
    'choice': 'Give the number, what do you want? ',
    'testpapers num':'How many types of testpapers do you need?  '}

# 3. Messages (errors not)
mesg = {
    'next':'Next step: ',
    'bad_arg_main':,
    'group name':'The name of the group is "%s".',
    'not_num':"You didn't wrote a(n integer) number!\n",
    'founded_exercises':'The exercise codes I found:',
    'not enough numbers':'It must be exercise in the groups!',
    'format':' Formats:\nIf you write pdf, ps or dvi, it uses the latex - dvips - ps2pdf programs\nIf you write pdflatex, you get a pdf format with pdflatex program\n If you write 0 or tex, it will not translate.\n',
    'with solution': '>'*55 +
                '\n\n If you want to print the exercises with solutions,\n'+
                 ' you must correct the signed row in the .tex file(s).\n\n' +
                '>'*55,
    'file_written':  'I wrote the exercises into the file "%s".\n',
    'found exercise_numbers': 'I found a base setting for the exercise numbers:',
    'series_in'   :  'Type in the exercisenumbers.\n',
    'fixed data'  :  '**** The data in the current form ****',
    'data'  :  '**** The data in the current form ****',
    'group name'  :  'The name of the group: "%s"',
       'modify'      : '''*** You can modify the brand new .tex file without brakeing the programm.
*** (eg. add or remove \\newpage)
*** If you are ready with it   PRESS >ENTER<
*** and the programm will continue.\n''',
       'foreword'      : ,
        'group'       :  'The exercises of the group "%s": %s',
        'version'     :  'This program expects at least Python 3.2.\n(www.python.org)'}



# Errors
err = {'endless definition' :
                'There is no end of definition at the input file.',
       'exercise missing':
                "There is no such exercise code: %d!",
       'not_num':
                'You didn\'t write an (integer) number!',
       'small num':
                'You have written a too small integer (minimum %d).',
       'large num':
                'You have written a too large integer (maximum %d).',
       'bad_arg':
                'Bad argument in "%s" at row %d.: "%s".',
       'bad_value':
                "You didn't write good values!",
       'bad boolean':
                "It isn't 'yes ' or 'not', I use the original.",
       'not enough numbers':
               'It must be minimum one exercise in a group!',
       'bad filename':
               'Bad filename: "%s", write a new one. ',
       'not filename':
               'There is no filename',
       'file not exists':
                       'Not an existing filename: "%s"',
       'not exercises':
                       'There isn\'t any exercises given.',
       'codes missing':
                       'Not all the codes are valid, check them.',
       'code run out':
                'There is no free code number! Ask for it!\n<horvath.arpad@amk.uni-obuda.hu>',
       'bad code'    :
                       'Bad exercise code at row %d',
       'no exercise'    :
                       'Bad exercisecode, there isn\'t such a code at file "%s"',
       'bad code2'    :
                       'Bad exercisecode "%s", there isn\'t such an exercise.',
       'not var'     :
                       'There isn\'t  %s képletben.',
       'uncomputable':
                       'There are uncomputable values at the exercise number %s.',
       'version'     :  'You need Python 2.0 or newer.\nYours is %s.\n(www.python.org)'}

# 4. The strings, which effects sg. (e.g. interrupt sg.)
#  Usually the lowercase forms are enough.
keys = {'quit':     ['q', 'quit'],
        'yes':    ['1', 1, 'y', 'yes'],
        'no':    ['n', '0', 0, 'no']}

todo = {
    'exercises and datas in':
    'Give me the exercise-numbers and some other data!',
    'test': 'I test the exercise codes',
    'substitute intervalls':
    'I make multiple testpapers with different values',
    'check again': 'I check this exercise again',
}
