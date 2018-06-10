from monitor import wsgi
from monitor import log
from monitor import conf
LOG = log.create_logger(conf.DEFAULT_API_LOG)

CONF = conf.CONF

class WSGIService(object):
    def __init__(self):
        self.loader = wsgi.Loader()
        self.app = self.loader.load_app()
        self.server = wsgi.Server(self.app,
                                  CONF.monitor_bind_ip,
                                  CONF.monitor_bind_port)
    def start(self):
        self.server.start()

    def wait(self):
        self.server.wait()

    def stop(self):
        self.server.stop()

def main():
    server = WSGIService()
    server.start()
    server.wait()

main()
