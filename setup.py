# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from setuptools import setup

# https://stackoverflow.com/questions/26737222/pypi-description-markdown-doesnt-work
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    long_description=long_description,
    setup_requires=['pytest-runner'],
    tests_require=['mock', 'pytest', 'pytest-cov'],
    package_data={
        'mirage_linemode': [
            'ranger_plugin/mirage_linemode.py',  # not package directory
            'template/*'
        ]
    }
)
