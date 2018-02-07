# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

import yaml
import re
from ranger.ext.widestring import WideString


# https://stackoverflow.com/questions/44875403/loading-special-characters-with-pyyaml
yaml.reader.Reader.NON_PRINTABLE = re.compile(
    u'[^\x09\x0A\x0D\x20-\x7E\x85\xA0-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]')  # noqa: E501


# https://stackoverflow.com/questions/2890146/how-to-force-pyyaml-to-load-strings-as-unicode-objects
def construct_yaml_str(self, node):
    # Override the default string handling function
    # to always return str objects
    ret = self.construct_scalar(node)
    return ret if isinstance(ret, str) else ret.encode('utf-8')


yaml.Loader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)
yaml.SafeLoader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)

theme_icon_skelton = {
    'file': '',
    'directory': '',
    'attr': {},
    'extension': {},
    'file_custom': {},
    'directory_custom': {},
    'parent_directory': {},
    'xdg_user_dirs': {}
}


def get_line(k, v):
    keys = '.'.join(k)

    return '{wlen:>2} | {value} | {keys}'.format(
        wlen=len(WideString(v)),
        value=v,
        keys=keys
    )


# def get_head():
#     return \
#         ' len | ch | keys name\n' + \
#         '---- | -- | ---------'

def isicon(v):
    ret = False
    try:
        if isinstance(v, str) or isinstance(v, unicode):
            ret = True
    except NameError:
        if isinstance(v, str):
            ret = True
    return ret


def print_list(theme_filename):
    try:
        with open(theme_filename, 'r') as fp:
            theme = yaml.load(fp)
    except (OSError, IOError, yaml.YAMLError):
        theme = {'icon': {}}
    theme_icon = theme['icon']

    # print(get_head())
    for k in theme_icon_skelton:
        if k in theme_icon and theme_icon[k]:
            v = theme_icon[k]
            if isicon(v):
                print(get_line([k], v))
            else:
                for i, w in v.items():
                    print(get_line([k, i], w))


if __name__ == '__main__':  # pragma: no cover.
    print_list({
        'file': 'f',
        'attr': {
            'py': 'PY',
            'c': 'C'
        }
    })
