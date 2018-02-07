# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

# from unittest import mock
# Mock = mock.Mock
import os
import pytest

config_filename_dummy = 'test_config.yml'
config_filename_no_exist = 'test_config_no_exit.yml'
theme_filename_dummy = 'test_theme.yml'
theme_filename_no_exist = 'test_theme_no_exist.yml'


@pytest.fixture
def config_path_dummy():
    script_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_path, config_filename_dummy)


@pytest.fixture
def config_path_no_exist():
    script_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_path, config_filename_no_exist)


@pytest.fixture
def theme_path_dummy():
    script_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_path, theme_filename_dummy)


@pytest.fixture
def theme_path_no_exist():
    script_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_path, theme_filename_no_exist)
