#coding:utf-8
import time
class allData(object):
    # 初始化数据
    def __init__(self):
        pass

    @classmethod
    def changeIntoStr(cls, data, str_data=''):
        if isinstance(data, unicode):
            str_data = data.encode('utf-8')
        elif isinstance(data, str):
            str_data = data
        return str_data

    @classmethod
    def createName(self, name):
        """
        :return:返回自动创建名字
        """
        couponName = name + str(int(time.time()))
        return couponName

    @property
    def getNowTime(self):
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return nowTime

    @property
    def createGoodName(self):
        """
        :return:返回自动创建名字
        """
        goodName = u"自动" + str(int(time.time()))
        return goodName

    @classmethod
    def create_publish(cls):
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        afterTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()+ 3 * 24 * 60 * 60))
        return nowTime,afterTime

    @classmethod
    def createRedGiftTime(cls, T):
        """
        :return: 返回发放开始时间，发放结束时间，可使用开始时间，可使用结束时间
        """
        if isinstance(T, str):
            T = int(T)
        grantStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 9 * 60 * 60))
        useStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 10 * 60 * 60))
        useEnd = grantEnd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + T * 24 * 60 * 60))
        return grantStart, grantEnd, useStart, useEnd

    @classmethod
    def createCouponTime(cls):
        """
        税换开始时间>可用开始时间
        :return: 返回发放开始时间，发放结束时间，可使用开始时间，可使用结束时间
        """
        grantStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 24 * 60 * 60))
        useStart = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        useEnd = time.strftime('%Y-%m-%d', time.localtime(time.time() + 7 * 24 * 60 * 60))
        grantEnd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 7 * 24 * 60 * 60))
        return grantStart, grantEnd, useStart, useEnd