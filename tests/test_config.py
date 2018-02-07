# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from mirage_linemode.config import (
    get_config
)


class TestConfig:
    def test_get_config(self, config_path_dummy, config_path_no_exist):
        config = get_config(config_path_dummy)
        assert config['fix_chars_width']['enabled']
        assert config['fix_chars_width']['for_term'] == {
            'default': ['a', 'b', 'c']
        }
        assert config['fix_chars_width']['for_both'] == {
            'default': set()
        }

        config = get_config(config_path_no_exist)
        assert config['fix_chars_width']['enabled'] is False
        assert config['fix_chars_width']['for_term'] == {
            'default': set()
        }
        assert config['fix_chars_width']['for_both'] == {
            'default': set()
        }
