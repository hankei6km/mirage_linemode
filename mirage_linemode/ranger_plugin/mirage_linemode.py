# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from __future__ import (absolute_import, division, print_function)

import ranger.api
from ranger.core.linemode import LinemodeBase
# from ranger.ext.human_readable import human_readable

import os

from mirage_linemode.config import (
    get_config
)

from mirage_linemode.theme.core import (
    get_theme
)

from mirage_linemode.util import (
    plugin_name,

    get_theme_path,
    get_config_path
)

# if 'RANGER_PTVSD' in os.environ:
#     import ptvsd
#     ptvsd.enable_attach(secret="my_secret", address=('0.0.0.0', 3000))
#     ptvsd.wait_for_attach()


def get_icon(theme_icon, fobj, metadata):
    if fobj.is_directory:
        icon = theme_icon['directory_custom'].get(fobj.relative_path, '')
    else:
        icon = theme_icon['file_custom'].get(fobj.relative_path, '')

    if icon == '':
        parent_directory = os.path.basename(os.path.dirname(fobj.path))
        icon = theme_icon['parent_directory'].get(parent_directory, '')

    if icon == '':
        icon = theme_icon['extension'].get(fobj.extension, '')

    if icon == '':
        icon = theme_icon['extension'].get(fobj.extension, '')

    if icon == '':
        for attr_name in theme_icon['attr']:
            if getattr(fobj, attr_name, False):
                icon = theme_icon['attr'][attr_name]

    if icon == '':
        icon = theme_icon['file']
        if fobj.is_directory:
            icon = theme_icon['directory']

    return icon


config = get_config(get_config_path())
config_fix_chars_width = config['fix_chars_width']
theme = get_theme(get_theme_path())
theme_icon = theme['icon']


HOOK_INIT_OLD = ranger.api.hook_init


def hook_init(fm):
    if config['default_linemode']['enabled']:
        fm.execute_console("default_linemode mirage")
    return HOOK_INIT_OLD(fm)


ranger.api.hook_init = hook_init


@ranger.api.register_linemode
class MarksideLinemode(LinemodeBase):
        name = plugin_name
        uses_metadata = False

        def filetitle(self, fobj, metadata):
            title = fobj.relative_path
            icon = get_icon(theme_icon, fobj, metadata)
            if config_fix_chars_width['enabled'] and \
                    (icon in config_fix_chars_width['for_term']['default'] or
                     icon in config_fix_chars_width['for_both']['default']):
                icon = icon + ' '

            return theme['line_format'].format(
                icon=icon,
                title=title
            )

        def infostring(self, fobj, metadata):
            if config_fix_chars_width['enabled'] and \
                    config_fix_chars_width['force_right_align']:
                ret = fobj.infostring

                icon = get_icon(theme_icon, fobj, metadata)
                if ret is not None and \
                        icon in config_fix_chars_width['for_term']['default']:
                    None
                else:
                    # ret = ret[:-1]
                    ret = ret + ' '

                return ret
            else:
                raise NotImplementedError
