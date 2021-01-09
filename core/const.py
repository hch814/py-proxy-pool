# -*- coding: utf-8 -*-
"""
constants

@author: hch
@date  : 2021/1/8
"""
from os import getenv
from os.path import dirname

import yaml


class Const:
    PROFILE = getenv("PROFILE", "dev")
    BASE_DIR = dirname(dirname(__file__))
    with open(f'{BASE_DIR}/conf/app-{PROFILE}.yml', 'r')as f:
        CONF = yaml.load(f, Loader=yaml.FullLoader)
        del f

    @classmethod
    def show(cls):
        for k, v in vars(Const).items():
            if not k.startswith("_") and not isinstance(v, classmethod):
                print(k, ':', v)
