# encoding: utf-8
## lang can be
## en        = english
## hu        = hungarian

import sys

lang = 'en'
lang = 'hu'

env = {
    'exercise': 'exercise',
    'solution': 'solution',
    'group': 'exercisegroup'}

if lang in [ 'magyar', 'hu']:
    preamble_file = "magyarpreambulum"
    env = {'exercise':'feladat',
        'solution':'megold',
        'group'   :'feladatcsoport'}
elif lang in ['english', 'en']:
    preamble_file = "preamble"
else:
    ValueError('No good settings for language in lang.py, I use Hungarian language.')
