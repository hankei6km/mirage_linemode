# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from __future__ import (absolute_import, division, print_function)

from os import path
from copy import deepcopy

from mirage_linemode.util import (
    mix_dict,
    yaml
)

from subprocess import CalledProcessError
from ranger.ext import spawn

fallback_xdg_user_dirs = {
    'DESKTOP': 'Desktop',
    'DOCUMENTS': 'Documents',
    'DOWNLOAD': 'Downloads',
    'MUSIC': 'Music',
    'PICTURES': 'Pictures',
    'PUBLICSHARE': 'Public',
    'TEMPLATES': 'Templates',
    'VIDEOS': 'Videos',
}

theme_skelton = {
    'line_format': '{icon} {title}',
    'icon': {
        'file': '📄',
        'directory': '📁',
        'attr': {},
        'extension': {},
        'file_custom': {},
        'directory_custom': {},
        'parent_directory': {},
        'xdg_user_dirs': {}
    }
}

default_theme = {
    'line_format': '{icon} {title}',
    'icon': {
        'file': '📄',
        'directory': '📁',
        'attr': {
        },
        'extension': {
        },
        'file_custom': {
        },
        'directory_custom': {
        },
        'parent_directory': {
            'home': '🏠'
        },
        'xdg_user_dirs': {
            'DESKTOP': '🕳️',
            'DOCUMENTS': '🗃️',
            'DOWNLOAD': '⬇️',
            'MUSIC': '🎼',
            'PICTURES': '🖼️',
            'PUBLICSHARE': '🏞️',
            'TEMPLATES': '📐',
            'VIDEOS': '🎬'
        }
    }
}


def spawn_xdg_user_dir(arg, default):
    ret = ''
    try:
        ret = spawn.check_output(['xdg-user-dir', arg]).strip()
    except AttributeError:
        try:
            ret = spawn.spawn(['xdg-user-dir', arg]).strip()
        except (OSError, CalledProcessError):
            ret = default
    except (OSError, CalledProcessError):
        ret = default
    ret = path.basename(ret)
    return ret


def get_xdg_user_dirs():
    ret = {
        k: spawn_xdg_user_dir(k, v)
        for k, v in fallback_xdg_user_dirs.items()
    }
    return ret


def get_theme(theme_path):
    src = deepcopy(theme_skelton)
    try:
        with open(theme_path, 'r') as fp:
            theme = mix_dict(src, yaml.load(fp))
    except (OSError, IOError, TypeError, yaml.YAMLError):
        theme = mix_dict(src, default_theme)
    # except:
    #     import sys
    #     exc = "Unexpected error:", sys.exc_info()[0]
    #     print(exc)
    #     theme = default_theme
    xdg_user_dirs = get_xdg_user_dirs()
    for k, v in xdg_user_dirs.items():
        if k in theme['icon']['xdg_user_dirs']:
            theme['icon']['directory_custom'][v] = \
                theme['icon']['xdg_user_dirs'][k]
    return theme
