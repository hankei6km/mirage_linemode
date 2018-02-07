# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

import mock
from mirage_linemode.ranger_plugin.mirage_linemode import get_icon
Mock = mock.Mock


class TestMirageLinemode:
    def test_get_icon(self):
        theme_icon = {
            'file': 'file_icon',
            'directory': 'dir_icon',
            'attr': {
            },
            'extension': {
                'md': 'md_icon'
            },
            'file_custom': {
                'f1': 'file_custom_icon'
            },
            'directory_custom': {
                'd1': 'dir_custom_icon'
            },
            'parent_directory': {
                'home': 'home_icon'
            },
        }
        fobj = Mock()

        fobj.path = '/test/test.txt'
        fobj.relative_path = 'test.txt'
        fobj.extension = 'txt'
        fobj.is_directory = False
        assert get_icon(
            theme_icon,
            fobj,
            Mock()
        ) == 'file_icon'

        fobj.is_directory = True
        assert get_icon(
            theme_icon,
            fobj,
            Mock()
        ) == 'dir_icon'

        fobj.extension = 'md'
        fobj.is_directory = False
        assert get_icon(
            theme_icon,
            fobj,
            Mock()
        ) == 'md_icon'

        fobj.path = '/home/foo'
        fobj.relative_path = 'foo'
        fobj.extension = ''
        fobj.is_directory = True
        assert get_icon(
            theme_icon,
            fobj,
            Mock()
        ) == 'home_icon'

        fobj.path = '/home/foo/f1'
        fobj.relative_path = 'f1'
        fobj.is_directory = False
        assert get_icon(
            theme_icon,
            fobj,
            Mock()
        ) == 'file_custom_icon'

        fobj.path = '/home/foo/d1'
        fobj.relative_path = 'd1'
        fobj.is_directory = False
        assert get_icon(
            theme_icon,
            fobj,
            Mock()
        ) == 'file_icon'

        fobj.path = '/home/foo/d1'
        fobj.relative_path = 'd1'
        fobj.is_directory = True
        assert get_icon(
            theme_icon,
            fobj,
            Mock()
        ) == 'dir_custom_icon'
