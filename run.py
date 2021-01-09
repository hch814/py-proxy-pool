from multiprocessing import Process

from controller.proxy import app
from core.const import Const
from service.proxy import ProxyService


def add_proxy():
    service = ProxyService()
    service.add_proxy()


def check_proxy():
    service = ProxyService()
    service.check_proxy()


if __name__ == '__main__':
    Const.show()
    Process(target=check_proxy).start()
    Process(target=add_proxy).start()
    app.run(host=Const.CONF['server']['ip'], port=Const.CONF['server']['port'])
