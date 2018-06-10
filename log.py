# -*- coding: utf8 -*-
import logging
from monitor import conf

def create_logger(path = conf.DEFAULT_API_LOG): 
    '''创建一个logger
    '''
    logger = logging.getLogger('monitor')
    logger.setLevel(logging.DEBUG)
     
    """创建一个handler，用于写入日志文件"""
    if not logger.handlers:
        wrHandler = logging.FileHandler(path)
        wrHandler.setLevel(logging.DEBUG)
     
        """再创建一个handler，用于输出到控制台，仅输出错误信息"""
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.WARNING)
     
        """定义handler的输出格式"""
        formatter_f = logging.Formatter('[%(asctime)s][%(process)d:%(thread)d][%(levelname)s] %(message)s')
        wrHandler.setFormatter(formatter_f)
        formatter_c = logging.Formatter('%(levelname)s: %(message)s')
        consoleHandler.setFormatter(formatter_c)
     
        """给logger添加handler"""
        logger.addHandler(wrHandler)
        logger.addHandler(consoleHandler)
    
    return logger 

'''
logger.debug('debug') 
logger.info('info') 
logger.warning('warning') 
logger.error('error') 
logger.critical('critical') 
'''
