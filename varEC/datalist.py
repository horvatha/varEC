"""
########################################
##
##  A class for setting up the programm
##
########################################
"""
from __future__ import print_function


class DataList:
    newline = '\n ---> '

    def __init__(self, text='Give me these dates:', type='text'):
        self.text = text

        self.type = type
        # Type  can be text, boolean and  "boolean row"
        # "boolean row" will be a boolean type, where
        # booleans depends on other booleans eg. one is false
        # an other must be false

        self.list = []

    def append(self, abbr, text, default):
        self.list.append([abbr, text])
        exec('self.' + abbr + '=' + repr(default))

    def __str__(self):
        string = self.text + ':\n'
        for abbr, text in self.list:
            value = eval("self." + abbr)
            string = string + '%s : "%s"\n' % (text, value)
        return string
