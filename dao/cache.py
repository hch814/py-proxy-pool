# -*- coding: utf-8 -*-
"""
cache

@author: hch
@date  : 2021/1/8
"""
import redis

from core.const import Const
from core.decorators import singleton


@singleton
class RedisDao:
    def __init__(self):
        host_port = Const.CONF['redis']['server'].split(":")
        max_conn = Const.CONF['redis']['max-pool-size']
        self.conn = redis.StrictRedis(host_port[0], host_port[1], max_connections=max_conn)


if __name__ == '__main__':
    r1 = RedisDao()
    r2 = RedisDao()
    r3 = RedisDao()
    print(r1.conn.zadd('zstest', {'mysql': 3}))
