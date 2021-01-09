# -*- coding: utf-8 -*-
"""
proxy controller

@author: hch
@date  : 2021/1/9
"""
from flask import Flask, request

from service.proxy import ProxyService

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/proxy', methods=['GET'])
def get():
    proxy = ProxyService().get_proxy()
    if proxy:
        return proxy
    else:
        return '', 404


@app.route('/proxy', methods=['DELETE'])
def delete():
    ProxyService().delete_proxy(request.args.get('key'))
    return 'ok'
