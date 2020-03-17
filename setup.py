#!/usr/bin/env python3

"""Test, build, or install the SerialComs package.
Run tests:
  python setup.py test
Build and install:
  python setup.py build && python setup.py install
"""

from distutils.util import convert_path
from setuptools import setup

VER_FILEPATH = convert_path('serialcoms/version.txt')
with open(VER_FILEPATH) as file:
    __version__ = file.read()

setup(
    name='SerialComs',
    description='A lightweight serial communications wrapper',
    url='https://github.com/texruska/SerialComs',
    author='Steven Burnett',
    license='GPLv3',
    author_email='texruska@users.noreply.github.com',
    packages=['serialcoms'],
    setup_requires=['pytest-runner'],
    tests_require=[
        'coverage',
        'pytest',
        'pytest-cov',
        'pytest-pylint'
    ],
    version=__version__,
    zip_safe=False
)
