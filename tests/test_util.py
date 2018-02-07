# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

import os
from xdg import BaseDirectory
# import pytest
# from unittest import mock

from mirage_linemode.util import (
    plugin_name_full,
    config_filename,
    theme_filename,
    mix_dict,
    get_config_path,
    get_theme_path
)

class TestUtil:
    def test_mix_dict(self):
        assert mix_dict({}, {}) == {}

        assert mix_dict(
            {'item1': 1},
            {}
        ) == {'item1': 1}

        assert mix_dict(
            {},
            {'item1': 2},
        ) == {'item1': 2}

        assert mix_dict(
            {'item1': 1},
            {'item1': 2},
        ) == {'item1': 2}

        assert mix_dict(
            {'item1': 1},
            {'item3': 2},
        ) == {
            'item1': 1,
            'item3': 2
        }

        assert mix_dict(
            {
                'item1': 1,
                'item2': 2,
                'grp1': {
                    'item1': 10,
                    'item2': 20
                },
                'grp2': {
                    'item3': 30,
                    'item4': 40
                }
            },
            {
                'item1': 5,
                'item3': 3,
                'grp1': {
                    'item1': 51,
                    'item3': 31
                },
                'grpr3': {
                    'item5': 30,
                    'item6': 60
                }
            },
        ) == {
            'item1': 5,
            'item2': 2,
            'item3': 3,
            'grp1': {
                'item1': 51,
                'item2': 20,
                'item3': 31
            },
            'grp2': {
                'item3': 30,
                'item4': 40
            },
            'grpr3': {
                'item5': 30,
                'item6': 60
            }
        }

    def test_get_config_path(self):
        assert os.path.join(
            BaseDirectory.xdg_config_home,
            *(plugin_name_full, config_filename)
        ) == get_config_path()

    def test_get_theme_path(self):
        assert os.path.join(
            BaseDirectory.xdg_config_home,
            *(plugin_name_full, theme_filename)
        ) == get_theme_path()
