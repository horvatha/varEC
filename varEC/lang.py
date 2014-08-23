# encoding: utf-8
## lang can be
## en        = english
## hu        = hungarian
from __future__ import print_function

lang = 'en'
lang = 'hu'


import sys
sys.path.append('./bin')
if lang in [ 'magyar', 'hu']:
    from .lang_hu import *
    preamble_file = "magyarpreambulum"

elif lang in [ 'english', 'en']:
    from .lang_en import *
    preamble_file = "preamble"

else:
    print('No good settings for language in lang.py, I use Hungarian language.')
    from .lang_hu import *
    preamble_file = "magyarpreambulum"
