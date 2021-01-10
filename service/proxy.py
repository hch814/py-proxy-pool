# -*- coding: utf-8 -*-
"""
proxy service

@author: hch
@date  : 2021/1/9
"""
import random
import time

import requests

from core.const import Const
from core.decorators import singleton
from dao.cache import RedisDao


@singleton
class ProxyService:
    def __init__(self):
        self.redis = RedisDao()
        self.key = Const.CONF['redis']['ip-pool-key']

    def add_proxy(self):
        while True:
            p, t = self.spider_proxy_zhima()
            if p:
                self.redis.conn.zadd(self.key, {p: t})
            time.sleep(1.7)

    def delete_proxy(self, *p):
        self.redis.conn.zrem(self.key, *p)

    def check_proxy(self):
        while True:
            expired_proxies = self.redis.conn.zrangebyscore(self.key, 0, int(time.time()))
            if expired_proxies:
                self.delete_proxy(*expired_proxies)
            time.sleep(1)

    def get_proxy(self):
        proxies = self.redis.conn.zrevrange(self.key, 0, 10)
        if proxies:
            return random.choice(proxies)

    def spider_proxy_zhima(self):
        zhima_url = self.redis.conn.hget(Const.CONF['proxy']['zhima'], "url")
        zhima_time = int(self.redis.conn.hget(Const.CONF['proxy']['zhima'], "alive-time"))
        resp = requests.get(zhima_url)
        if resp.status_code == 200 and not resp.text.startswith("{"):
            r = resp.text.strip()
            print('zhima:', r)
            return r, int(time.time()) + zhima_time
        else:
            return None, None


if __name__ == '__main__':
    print(ProxyService().redis.conn.hgetall(Const.CONF['proxy']['zhima']).get(b'url'))
