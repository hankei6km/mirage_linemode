# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from __future__ import (absolute_import, division, print_function)

from copy import deepcopy

from mirage_linemode.util import (
    mix_dict,
    yaml
)


default_config = {
    'default_linemode': {
        'enabled': True
    },
    'fix_chars_width': {
        'enabled': False,
        'force_right_align': False,
        'for_term': {
            'default': set()
        },
        'for_py': {
            'default': set()
        },
        'for_both': {
            'default': set()
        }
    }
}


def get_config(config_path):
    src = deepcopy(default_config)
    try:
        with open(config_path, 'r') as fp:
            config = mix_dict(src, yaml.load(fp))
    except (OSError, IOError, TypeError, yaml.YAMLError):
        config = src
    # except:
    #     import sys
    #     exc = "Unexpected error:", sys.exc_info()[0]
    #     print(exc)
    #     config = src
    return config
