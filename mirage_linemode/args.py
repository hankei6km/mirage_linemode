# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

import sys
import os
import configparser
import pkg_resources
import argparse
# from urllib.parse import urlparse
# import re

metadata = {
    'name': 'mirage_linemode',
    'description':
        'Customizable linemode plugin for ranger.',
    'version': ''
}

try:
    script_path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(script_path), 'setup.cfg'))
    metadata['version'] = config['metadata']['version']
except KeyError:  # pragma: no cover.
    None

try:
    metadata['version'] = pkg_resources.get_distribution(
        metadata['name']
    ).version
except pkg_resources.DistributionNotFound:  # pragma: no cover.
    None

parser = argparse.ArgumentParser(prog=metadata['name'],
                                 description=metadata['description'])

parser.add_argument('--version',
                    action='version',
                    version='%(prog)s version ' + metadata['version'])

subparsers = parser.add_subparsers(help='sub-command help')

parser_init = subparsers.add_parser('init',
                                    help='Copy initialized files '
                                    'into config directory'
                                    '(ie. '
                                    '$HOME/.config/midage_linemode)')
parser_init.add_argument('-o', '--overwrite',
                         dest='overwrite',
                         action='store_true')

parser_enable = subparsers.add_parser('enable',
                                      help='Enable plugin on ranger')

parser_disable = subparsers.add_parser('disable',
                                       help='Disable plugin on ranger')

parser_theme = subparsers.add_parser('theme',
                                     help='Work to theme')

parser_theme.add_argument('-w',
                          dest='icon_width_list',
                          action='store_true',
                          help='Display chars width list')


def parse(argv, funcs):
    parser_init.set_defaults(func=funcs['init'])
    parser_enable.set_defaults(func=funcs['enable'])
    parser_disable.set_defaults(func=funcs['disable'])
    parser_theme.set_defaults(func=funcs['theme'])
    args = parser.parse_args(argv)
    return args


if __name__ == '__main__':  # pragma: no cover.
    args = parse(sys.argv[1:], {
        'init': lambda args: True,
        'enable': lambda args: True,
        'disable': lambda args: True,
        'theme': lambda args: True
    })
    print(args)
