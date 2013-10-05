#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

if sys.version_info < (2, 6):
    print("This module requires Python >= 2.6")
    sys.exit(0)

description="""
The cxnet extends IGraph module with some functionality
I am using in higher education.
Some functionality is available with NetworkX module as well.
Function plotting needs matplotlib (pylab).

Functionalities:
- Creating networks with multifractal network generator.
- Creating network from the deb package hierarchy.
- Investigating and plotting degree distribution.
- Graph methods:

 * to list the vertices with most degrees,
 * to plot the neighbours of a vertex.

- A tool to create network evolution models.
"""

options = dict(
    name = 'varEC',
    version = '0.1',
    description = 'Test paper variations maker using LaTeX',
    long_description = description,
    license = 'BSD License',

    author = 'Arpad Horvath',
    author_email = 'horvath.arpad.szfvar@gmail.com',
    url = 'http://django.arek.uni-obuda.hu/',

    packages = ['varEC' ],
    #scripts = ['scripts/ec-sorter.py', 'scripts/ec-coder.py', 'scripts/ec-tryexercise.py'],
    #test_suite = "igraph.test.suite",

    platforms = 'ALL',
    keywords = ['LaTeX', 'education', 'mathematics', 'physics', 'higher education', 'quiz', 'test paper'],
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Education',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Mathematics',
      'Topic :: Scientific/Engineering :: Physics',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'License :: OSI Approved :: BSD License',
    ]
)

setup(**options)
