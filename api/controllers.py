#-*- coding: utf-8 -*-
from oslo_config import cfg
import webob
import simplejson
import commands
from webob.dec import wsgify
from webob import exc
from monitor import conf
from monitor import log

LOG = log.create_logger(conf.DEFAULT_API_LOG)

CONF = conf.CONF

class Controller(object):
    def __init__(self):
	pass
    
    def start_monitor(self, req):
        """启用监控
        """
	"""TODO:开启监控进程"""
        return {"status": "200", "msg": "启用成功"}

    def stop_monitor(self, req):
        """关闭监控
        """
	"""TODO:关闭监控进程"""
        return {"status": "200", "msg": "关闭成功"}

    def get_monitor(self, req):
        """获取监控数据
        """
	"""TODO:查询数据库获取监控数据"""
	detail = [] #监控数据
        return {"status": "200", "msg": "获取成功", "detail": detail}

    @wsgify(RequestClass=webob.Request)    
    def __call__(self, req):
        arg_dict = req.environ['wsgiorg.routing_args'][1]
        action = arg_dict.pop('action')
        del arg_dict['controller']

        method = getattr(self, action)
        result = method(req, **arg_dict)

        if result is None:
            return webob.Response(body='',
                                  status='204 Not Found',
                                  headerlist=[('Content-Type',
                                               'application/json')])
        if result == '200':
            return webob.Response(body='',
                                  status='200 OK',
                                  headerlist=[('Content-Type',
                                               'application/json')])
        if result == '202':
            return webob.Response(body='',
                                  status='202 Accepted',
                                  headerlist=[('Content-Type',
                                               'application/json')])
        
        else:
            if not isinstance(result, basestring):
                result = simplejson.dumps(result)
            return result

