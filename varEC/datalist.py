"""
########################################
##
##  A class for setting up the programm
##
########################################
"""
from __future__ import print_function
from .lang import lang
from .message import cls #error, ask, message

try:
    input = raw_input
except NameError:
    pass

try:
  exec('from .lang_%s import *' % lang)
except ImportError:
  print("datalist: There's no lang_%s, I use lang_en" % lang)
  from .lang_en import *

# Here should be lang, not lang_hu, but lang import from setup,
# setup import datalist. How can I solve the problem?

import string

class DataList:
    newline = '\n ---> '
    def __init__(self, text = 'Give me these dates:', type='text'):
        self.text = text

        self.type = type
        # Type  can be text, boolean and  "boolean row"
        # "boolean row" will be a boolean type, where
        # booleans depends on other booleans eg. one is false
        # an other must be false

        self.list = []

    def append(self, abbr, text, default):
        self.list.append( [abbr, text] )
        exec('self.'+ abbr + '=' + repr(default))

    def query(self):
        print('**** ' + self.text + ' ****')
        #print("Datalist type: %s" % self.type)
        for num in range(len(self.list)):
            abbr, text = self.list[num]
            exec("default = self." + abbr)
            if self.type in ('boolean',  'boolean row'):
                answer = self.boolean_query(text, default)
            elif self.type == 'text':
                answer = self.plain_quiery(text, default)
            else:
                raise ValueError("bad datalist type")
            exec('self.'+abbr + ' = ' + repr(answer))
            if self.type == 'boolean row' and answer == 0:
                self.set_the_rest_false(num + 1)
                return

    def set_the_rest_false(self, num):
        """It set the boolean variable to false from "num"-th data."""
        for i in range(num, len(self.list)):
            abbr, text = self.list[num]
            exec('self.%s = 0' % abbr)

    def plain_quiery(self, text, default):
        answer = input('** %s\n (Enter = "%s"): ' % (text, default) )
        answer = answer or default
        return answer

    def boolean_query(self, text, default):
        if default in keys['yes']:
            default = keys['yes'][0]
        elif default in keys['no']:
            default = keys['no'][0]
        else:
            print("Boolean: %s, type: %s" % (default, self.type))
            raise ValueError("the value of an boolean data is not good")

        answer = input('** %s\n (Enter = "%s"): ' % (text, default) )
        answer = answer or default
        answer =  string.lower(answer)
        if answer in keys['yes']:
            answer = 1
        elif answer in keys['no']:
            answer = 0
        else:
            print(err['bad boolean'])
            answer = default
        return answer

    def __str__(self):
        string = self.text + ':\n'
        for abbr, text in self.list:
            exec("value = self." +abbr)
            if self.type in ('boolean',  'boolean row'):
                if value in keys['yes']:
                    value = keys['yes'][0]
                elif value in keys['no']:
                    value = keys['no'][0]
            #string = string + '(%s) %s : "%s"\n' % (abbr, text, value)
            string = string + '%s : "%s"\n' % (text, value)
        return string

    def setup(self):
        answer = keys['yes'][0]
        while 1:
            cls()
            print(mesg['data'])
            print(self)
            answer = string.lower(input(ask['change']) )
            if answer in keys['no'] or answer == '':
                return
            self.query()
