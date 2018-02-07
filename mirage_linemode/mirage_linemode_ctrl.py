# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.
import os
import shutil
from xdg import BaseDirectory

from mirage_linemode.util import (
    get_config_path,
    get_theme_path,
)
from mirage_linemode.theme.icon_width_list import print_list


class MirageLinemodeControl:

    def __init__(self):
        from mirage_linemode.util import (
            ranger_name,
            plugin_name,
            plugin_name_full,

            plugin_filename,
            config_filename,
            theme_filename,

            plugin_path_in_pkg,
            config_path_in_pkg,
            theme_path_in_pkg,
        )
        self._ranger_name = ranger_name
        self._plugin_name = plugin_name
        self._plugin_name_full = plugin_name_full
        self._plugin_filename = plugin_filename
        self._config_filename = config_filename
        self._theme_filename = theme_filename
        self._plugin_path_in_pkg = plugin_path_in_pkg
        self._config_path_in_pkg = config_path_in_pkg
        self._theme_path_in_pkg = theme_path_in_pkg

        try:
            path = next(BaseDirectory.load_config_paths(
                *(self._ranger_name, 'plugins')
            ))
        except StopIteration:
            path = os.path.join(
                BaseDirectory.xdg_config_home,
                *(self._ranger_name, 'plugins')
            )
        self._ranger_plugins_home = path

        try:
            path = next(BaseDirectory.load_config_paths(
                self._plugin_name_full
            ))
        except StopIteration:
            path = os.path.join(
                BaseDirectory.xdg_config_home, self._plugin_name_full
            )
        self._config_home = path

        script_path = os.path.dirname(__file__)
        self._plugin_path = os.path.join(script_path, self._plugin_path_in_pkg)
        self._config_path = os.path.join(script_path, self._config_path_in_pkg)
        self._theme_path = os.path.join(script_path, self._theme_path_in_pkg)

    def init(self, args):

        # copy config file and theme file `$HOME/.config/mirage_linemode`
        BaseDirectory.save_config_path(self._plugin_name_full)
        dst = get_config_path()
        if args.overwrite or os.access(dst, os.F_OK) is False:
            shutil.copy2(self._config_path, dst)
        dst = get_theme_path()
        if args.overwrite or os.access(dst, os.F_OK) is False:
            shutil.copy2(self._theme_path, dst)

    def enable(self, args):
        dst = os.path.join(self._ranger_plugins_home, self._plugin_filename)
        if os.access(dst, os.F_OK) is False:
            os.symlink(self._plugin_path, dst)

    def disable(self, args):
        dst = os.path.join(self._ranger_plugins_home, self._plugin_filename)
        if os.access(dst, os.F_OK) is True:
            os.remove(dst)

    def theme(self, args):
        if args.icon_width_list:
            theme_filename = \
                os.path.join(self._config_home, self._theme_filename)
            print(theme_filename)
            print_list(theme_filename)
