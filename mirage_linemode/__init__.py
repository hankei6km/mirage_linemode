# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

import sys
from mirage_linemode import args
from mirage_linemode.mirage_linemode_ctrl import MirageLinemodeControl


def main(argv=sys.argv[1:]):  # pragma: no cover.
    mlc = MirageLinemodeControl()
    funcs = {
        'init': mlc.init,
        'enable': mlc.enable,
        'disable': mlc.disable,
        'theme': mlc.theme
    }
    parsed_args = args.parse(argv, funcs)
    parsed_args.func(parsed_args)
    None
