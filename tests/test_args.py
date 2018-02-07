# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

# import pytest
# from unittest import mock
import mock
from mirage_linemode.args import parse

Mock = mock.Mock


class TestArgs:
    def test_parse(self):
        def get_funcs():
            return {
                'init': Mock(),
                'enable': Mock(),
                'disable': Mock(),
                'theme': Mock(),
            }

        funcs = get_funcs()
        parsed_args = parse(['init'], funcs)
        parsed_args.func(parsed_args)
        funcs['init'].assert_called_once()
        funcs['enable'].assert_not_called()
        funcs['disable'].assert_not_called()
        funcs['theme'].assert_not_called()

        funcs = get_funcs()
        parsed_args = parse(['enable'], funcs)
        parsed_args.func(parsed_args)
        funcs['init'].assert_not_called()
        funcs['enable'].assert_called_once()
        funcs['disable'].assert_not_called()
        funcs['theme'].assert_not_called()

        funcs = get_funcs()
        parsed_args = parse(['disable'], funcs)
        parsed_args.func(parsed_args)
        funcs['init'].assert_not_called()
        funcs['enable'].assert_not_called()
        funcs['disable'].assert_called_once()
        funcs['theme'].assert_not_called()

        funcs = get_funcs()
        parsed_args = parse(['theme'], funcs)
        parsed_args.func(parsed_args)
        funcs['init'].assert_not_called()
        funcs['enable'].assert_not_called()
        funcs['disable'].assert_not_called()
        funcs['theme'].assert_called_once()
