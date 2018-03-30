#coding:utf-8
import unittest

class SuperTest(unittest.TestCase):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    @classmethod
    def setUpClass(cls):
        """
        初始化数据
        :return:
        """
        pass
    @classmethod
    def tearDownClass(cls):
        pass