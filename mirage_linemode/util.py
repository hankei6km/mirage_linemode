# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from __future__ import (absolute_import, division, print_function)

from os import path
import yaml
import re

from xdg import BaseDirectory

ranger_name = 'ranger'

plugin_name = 'mirage'
plugin_name_full = plugin_name + '_linemode'

plugin_filename = plugin_name_full + '.py'
config_filename = plugin_name_full + '_config.yml'
theme_filename = plugin_name_full + '_theme.yml'

plugin_path_in_pkg = path.join('ranger_plugin', plugin_filename)
config_path_in_pkg = path.join('template', config_filename)
theme_path_in_pkg = path.join('template', theme_filename)

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


# https://stackoverflow.com/questions/7204805/dictionaries-of-dictionaries-merge/7205107#7205107
def mix_dict(a, b={}, path=[]):
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                mix_dict(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass  # same leaf value
            elif b[key] == '' or b[key] is None:
                pass  # blank leaf value
            else:
                a[key] = b[key]  # over write
        else:
            a[key] = b[key]
    return a


def get_theme_path():
    try:
        tmp = next(BaseDirectory.load_config_paths(plugin_name_full))
    except StopIteration:
        tmp = path.join(BaseDirectory.xdg_config_home, plugin_name_full)
    return path.join(
        tmp,
        theme_filename
    )


def get_config_path():
    try:
        tmp = next(BaseDirectory.load_config_paths(plugin_name_full))
    except StopIteration:
        tmp = path.join(BaseDirectory.xdg_config_home, plugin_name_full)
    return path.join(
        tmp,
        config_filename
    )
