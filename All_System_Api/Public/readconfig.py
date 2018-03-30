#coding:utf-8
import ConfigParser
import os
import shutil
from BaseRequest.BasePath import conf_path

#读取app.ini 中的packname、appActivity项

def removeall(rootdir):
    filelist=os.listdir(rootdir)
    for f in filelist:
        filepath = os.path.join( rootdir, f )
        if os.path.isfile(filepath):
            os.remove(filepath)
            print (filepath+" removed!")
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)
            print ("dir "+filepath+" removed!")

#读取配置文件中的信息
def read_config_info(conf,api,api_data):
    """
    :param conf: 配置文件名
    :param api: 文件内接口名
    :param data: 接口内参数名
    :return: 参数值
    """
    config= ConfigParser.ConfigParser()
    with open(os.path.join(conf_path,conf),'r') as cfgfile:
        config.readfp(cfgfile)
        getdata=config.get(api,api_data)
    return getdata

#保存配置文件中的
def write_config_info(conf,api,api_data,write_data):
    """
    :param conf: 配置文件名
    :param api: 文件内接口名
    :param api_data: 接口内参数名
    :param write_data: 写入参数的数据
    :return: None
    """
    config = ConfigParser.ConfigParser()
    with open(os.path.join(conf_path,conf),'r') as cfgfile:
        config.readfp(cfgfile)
        config.set(api,api_data,write_data)
        config.write(open(os.path.join(conf_path,conf),'w'))

if __name__=="__main__":
    import json
    print read_config_info('login_api.ini','login','data'),type(read_config_info('login_api.ini','login','data'))
    json.loads(read_config_info('login_api.ini', 'login', 'data'))