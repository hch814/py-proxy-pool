# -*- coding: utf-8 -*-
"""
decorators

@author: hch
@date  : 2021/1/8
"""


def singleton(cls):
    _instances = {}

    def __wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return __wrapper
