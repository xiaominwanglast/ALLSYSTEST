#coding=utf-8
import os
import logging
from functools import wraps
from BaseRequest.BasePath import log_path
def extra_log_function(func):
    """
    #类修饰器
    #修饰log输出格式
    :param func:
    :return:
    """
    @wraps(func)
    def _extra(self,url=None,rq_type=None,header_data=None,response_data=None):
        self.logger.info('--'*60)
        if url:
            self.logger.info(u'请求地址：'+url)
        if rq_type:
            self.logger.info(u'请求方式：'+rq_type)
        if header_data:
            if isinstance(header_data,dict) or isinstance(header_data,tuple):
                header_data=str(header_data)
            self.logger.info(u'请求数据：'+ header_data)
        if response_data:
            if isinstance(response_data, dict) or isinstance(response_data, tuple):
                response_data=str(response_data)
            self.logger.info(u'返回数据：'+response_data)
        self.logger.info('--' * 60)
    return _extra

def other_function(func):
    """
    #输出info,warning,error,debug信息格式
    :param func:
    :return:
    """
    @wraps(func)
    def _other(self,*args,**kwargs):
        func(self,*args,**kwargs)
    return _other

class Logger(object):
    def __init__(self,sys_name):
        """
        :param sys_name:
        """
        self.name='TestResult'
        self.logger = logging.getLogger('Api_Logger')
        self.format = '%(asctime)s [%(levelname)s] [{0}] %(message)s'.format(sys_name)
        fm = logging.Formatter(self.format)
        file_handler = logging.FileHandler('%s.log' % os.path.join(log_path, self.name), mode='a', encoding="UTF-8")
        file_handler.setFormatter(fm)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)

    @extra_log_function
    def log(self,url=None,rq_type=None,header_data=None,response_data=None):
        pass

    @other_function
    def Info(self, msg):
        self.logger.info(msg)

    @other_function
    def Warning(self, msg):
        self.logger.warning(msg)

    @other_function
    def Error(self, msg):
        self.logger.error(msg)

    @other_function
    def Debug(self, msg):
        self.logger.debug(msg)

if  __name__=="__main__":
    Logger('inventory_transport').Info('https://deposit.koudailc.com/deposit/account/remain')
