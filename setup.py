# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from setuptools import setup

# https://stackoverflow.com/questions/26737222/pypi-description-markdown-doesnt-work
try:
    import pypandoc
    with open('README.md', 'r') as fp:
        import re
        md = fp.read()
        md = re.sub(r'!\[.+\]\(.+\)', r'', md)
        long_description = pypandoc.convert_text(md, 'rst', format='md')
except(ImportError):
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
