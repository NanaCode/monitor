#-*- coding: utf-8 -*-
import routes
import routes.middleware
import webob
import webob.dec
from webob.dec import wsgify
import controllers

class Router(object):
    def __init__(self):
        
        self.mapper = routes.Mapper()
        self.add_routes()
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.mapper)
        
    def add_routes(self):
        controller = controllers.Controller()
       
        """启用监控"""
        self.mapper.connect("/monitor/start",
                           controller=controller, action="start_monitor",
                           conditions=dict(method=["POST"]))

        """关闭监控"""
        self.mapper.connect("/monitor/stop",
                           controller=controller, action="stop_monitor",
                           conditions=dict(method=["POST"]))

        """获取监控数据"""
        self.mapper.connect("/monitor",
                           controller=controller, action="get_monitor",
                           conditions=dict(method=["GET"]))

    @wsgify(RequestClass=webob.Request)
    def __call__(self, request):
        return self._router
        
    @staticmethod
    @wsgify(RequestClass=webob.Request)
    def _dispatch(request):
        match = request.environ['wsgiorg.routing_args'][1]
        if not match:
            return _err() 
        app = match['controller']
        return app

def _err():
    return 'The Resource is Not Found.'

def app_factory(global_config, **local_config):
    return Router()

