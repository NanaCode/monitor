import eventlet
import eventlet.wsgi
import greenlet
import socket
import sys
import os
from paste import deploy
from monitor import conf
from monitor import log
LOG = log.create_logger(conf.DEFAULT_API_LOG)

CONF = conf.CONF

class Loader(object):
    def load_app(self):
        ini_path = conf.PASTE_INI
        if not os.path.isfile(ini_path):
            print("Cannot find api-paste.ini.\n")
            LOG.error("Cannot find api-paste.ini.")
            exit(1)

        return deploy.loadapp('config:' + ini_path)

class Server(object):
    def __init__(self, app, host = '0.0.0.0', port = 8010):
        self._pool = eventlet.GreenPool(1000)
        self.app = app
        
        bind_addr = (host,port) 
        self._socket = eventlet.listen(bind_addr, backlog=128)
        (self.host, self.port) = self._socket.getsockname()
        
    def start(self):
        LOG.info("Starting monitor-api.")

        wsgi_kwargs = {
            'func': eventlet.wsgi.server,
            'sock': self._socket,
            'site': self.app,
            'protocol': eventlet.wsgi.HttpProtocol,
            'custom_pool': self._pool,
        }
        self._server = eventlet.spawn(**wsgi_kwargs)
        LOG.info("Started monitor-api.")

    def stop(self):
        if self._server is not None:
            self._pool.resize(0)
            self._server.kill()

    def wait(self):
        try:
            if self._server is not None: 
                self._pool.waitall()
                self._server.wait()
        except greenlet.GreenletExit:
            LOG.info("WSGI server has stopped.")

