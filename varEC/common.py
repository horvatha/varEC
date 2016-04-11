textdomain = '/home/ha/repo/varEC/locale'
import gettext
gettext.bindtextdomain('varEC', textdomain)
gettext.textdomain('varEC')
_ = gettext.gettext


class VarECException(Exception):
    """Base Exception. Just its children are used in the program."""
    pass


class LaTeXError(VarECException):
    def __init__(self, type_, code, row):
        self.type_ = type_
        self.code = code
        self.row = row

    def __str__(self):
        return """There is a bad %s in the exercise %s!
The format is %s{<base_value>}{<xxx>} and must be in one row!
The row is:
 %s""" % (self.type_, self.code, self.type_, self.row)


class BadCodeException(VarECException):
    def __init__(self, file_name, code, row):
        self.file_name = file_name
        self.code = code
        self.row = row

    def __str__(self):
        return _(
            'There is a bad code in file {file_name} in row {row}: "{code}"'
            ' Code must be integer.').format(
                row=self.row,
                code=self.code,
                file_name=self.file_name)


class CodeNotFoundError(VarECException):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return _("""Code %d can not be found.""") % (self.code)


class UncomputableError(VarECException):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return _('There are uncomputable values at the exercise number %s.')\
            % self.code


class EcSyntaxError(VarECException):
    def __init__(self, row):
        self.row = row

    def __str__(self):
        return """There is a syntax error in the table
in the row {0}.""".format(self.row)
