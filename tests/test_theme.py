# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from mirage_linemode.theme.core import (
    get_xdg_user_dirs,
    get_theme
)

import mock
Mock = mock.Mock


class TestTheme:
    @mock.patch(
        'mirage_linemode.theme.core.spawn_xdg_user_dir')
    def test_get_xdg_user_dirs(self, mock_spawn_xdg_user_dir):
        mock_spawn_xdg_user_dir.side_effect = lambda k, v: k + ';' + v
        assert get_xdg_user_dirs() == {
            'DESKTOP': 'DESKTOP;Desktop',
            'DOCUMENTS': 'DOCUMENTS;Documents',
            'DOWNLOAD': 'DOWNLOAD;Downloads',
            'MUSIC': 'MUSIC;Music',
            'PICTURES': 'PICTURES;Pictures',
            'PUBLICSHARE': 'PUBLICSHARE;Public',
            'TEMPLATES': 'TEMPLATES;Templates',
            'VIDEOS': 'VIDEOS;Videos',
        }

    @mock.patch(
        'mirage_linemode.theme.core.get_xdg_user_dirs')
    def test_get_theme(self,
                       mock_get_xdg_user_dirs,
                       theme_path_dummy,
                       theme_path_no_exist):
        mock_get_xdg_user_dirs.return_value = {
            'DESKTOP': 'デスクトップ',
            'DOCUMENTS': 'ドキュメント',
            'DOWNLOAD': 'ダウンロード',
            'MUSIC': 'ミュージック',
            'PICTURES': 'ピクチャ',
            'PUBLICSHARE': 'パブリック',
            'TEMPLATES': 'テンプレート',
            'VIDEOS': 'ビデオ',
        }
        theme = get_theme(theme_path_dummy)
        assert theme['line_format'] == 'test1'
        assert theme['icon']['file'] == 'test2'
        assert theme['icon']['directory'] == 'test3'
        assert theme['icon']['directory_custom']['デスクトップ'] == 'test4'

        theme = get_theme(theme_path_no_exist)
        assert theme['line_format'] == '{icon} {title}'
        assert theme['icon']['file'] == '📄'
        assert theme['icon']['directory'] == '📁'
        assert theme['icon']['directory_custom']['ドキュメント'] == '🗃️'
