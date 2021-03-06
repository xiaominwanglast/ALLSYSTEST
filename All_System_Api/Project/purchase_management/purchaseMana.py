#coding:utf-8
#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
import time
class PurchaseM(SuperTest):
    """新采购系统接口测试"""
    TestData=read_json('purchase_management.json')
    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],
                               headers=self.headers)
        self.assertTrue(login_res.status_code==200)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"])+'\n'+login_res.text)
        session.close()

    def test2(self):
        """城市商品管理展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            GoodsList_res=session.post(url=self.TestData["GoodsList"]["GoodsList_url"],data=self.TestData["GoodsList"]["GoodsList_data"])
            self.assertTrue(GoodsList_res.status_code==200)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test3(self):
        """供应商信息管理"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            GoodsList_res=session.post(url=self.TestData["GoodsList"]["GoodsList_url"],data=self.TestData["GoodsList"]["GoodsList_data"])
            self.assertTrue(GoodsList_res.status_code==200)
            Logger(self.TestData["name"]).Info(str(self.TestData["GoodsList"])+'\n'+GoodsList_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()


if __name__=='__main__':
    unittest.main()


