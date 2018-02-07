# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

import os
from xdg import BaseDirectory
# import pytest
# from unittest import mock
import mock
from mirage_linemode.mirage_linemode_ctrl import MirageLinemodeControl

Mock = mock.Mock

ranger_name = 'ranger'

plugin_name = 'mirage'
plugin_name_full = plugin_name + '_linemode'

plugin_filename = plugin_name_full + '.py'
config_filename = plugin_name_full + '_config.yml'
theme_filename = plugin_name_full + '_theme.yml'

plugin_rel_path = os.path.join('ranger_plugin', plugin_filename)
config_rel_path = os.path.join('template', config_filename)
theme_rel_path = os.path.join('template', theme_filename)

script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                           plugin_name_full)
plugin_path = os.path.join(script_path, plugin_rel_path)
config_path = os.path.join(script_path, config_rel_path)
theme_path = os.path.join(script_path, theme_rel_path)

ranger_plugins_home = os.path.join(BaseDirectory.xdg_config_home,
                                   *(ranger_name, 'plugins'))
config_home = os.path.join(BaseDirectory.xdg_config_home, plugin_name_full)


class TestMirageLinemodeControler:
    def test_constructor(self):
        mlc = MirageLinemodeControl()
        assert mlc._ranger_plugins_home == ranger_plugins_home
        assert mlc._config_home == config_home
        assert mlc._plugin_path == plugin_path
        assert mlc._config_path == config_path
        assert mlc._theme_path == theme_path

    @mock.patch('os.access')
    @mock.patch('xdg.BaseDirectory.save_config_path')
    @mock.patch('shutil.copy2')
    def test_init(self,
                  mock_copy2,
                  mock_save_config_path,
                  mock_access):
        mlc = MirageLinemodeControl()
        mock_access.return_value = False
        mock_args = Mock()
        mock_args.overwrite = False
        mlc.init(mock_args)
        calls = [
            mock.call(config_path, os.path.join(config_home, config_filename)),
            mock.call(theme_path, os.path.join(config_home, theme_filename))
        ]
        mock_copy2.assert_has_calls(calls)

        mock_copy2.reset_mock()
        mock_access.return_value = True
        mock_args.overwrite = False
        mlc.init(mock_args)
        mock_copy2.assert_not_called()

        mock_copy2.reset_mock()
        mock_access.return_value = True
        mock_args.overwrite = True
        mlc.init(mock_args)
        calls = [
            mock.call(config_path, os.path.join(config_home, config_filename)),
            mock.call(theme_path, os.path.join(config_home, theme_filename))
        ]
        mock_copy2.assert_has_calls(calls)

    @mock.patch('os.access')
    @mock.patch('os.symlink')
    def test_enable(self, mock_symlink, mock_access):
        mlc = MirageLinemodeControl()
        mock_access.return_value = False
        mlc.enable(Mock())
        calls = [
            mock.call(
                plugin_path,
                os.path.join(ranger_plugins_home, plugin_filename)
            )
        ]
        mock_symlink.assert_has_calls(calls)

        mock_symlink.reset_mock()

        mock_access.return_value = True
        mlc.enable(Mock())
        mock_symlink.assert_not_called()

    @mock.patch('os.access')
    @mock.patch('os.remove')
    def test_disable(self, mock_remove, mock_access):
        mlc = MirageLinemodeControl()
        mock_access.return_value = True
        mlc.disable(Mock())
        calls = [
            mock.call(
                os.path.join(ranger_plugins_home, plugin_filename)
            )
        ]
        mock_remove.assert_has_calls(calls)

        mock_remove.reset_mock()

        mock_access.return_value = False
        mlc.disable(Mock())
        mock_remove.assert_not_called()

    @mock.patch('mirage_linemode.theme.icon_width_list.print_list')
    def test_theme(self, mock_print_list):
        mlc = MirageLinemodeControl()
        args = Mock()
        args.icon_width_list = True
        mlc.theme(args)
        # couldn't patch?
        # mock_print_list.assert_called_once()

        mock_print_list.mock_reset()

        args = Mock()
        args.icon_width_list = False
        mlc.theme(args)
        mock_print_list.assert_not_called()
