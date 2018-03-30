#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
import time
class StoreM(SuperTest):
    """业务员系统接口测试"""
    TestData=read_json('store_management.json')
    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],
                               headers=self.headers)
        self.assertTrue(login_res.status_code==200)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"])+'\n'+login_res.text)
        session.close()

    def test2(self):
        """业务员列表信息显示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["changeCity"]["changeCity_url"],data=self.TestData["changeCity"]["changeCity_data"])
            salesmanList_res=session.post(url=self.TestData["salesmanList"]["salesmanList_url"],data=self.TestData["salesmanList"]["salesmanList_data"])
            salesmanList_json=json.loads(allData().changeIntoStr(salesmanList_res.text))
            self.assertTrue(salesmanList_res.status_code==200 and len(salesmanList_json["data"])>=1)
            Logger(self.TestData["name"]).Info(str(self.TestData["salesmanList"])+'\n'+salesmanList_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test3(self):
        """店铺类型信息显示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["changeCity"]["changeCity_url"],data=self.TestData["changeCity"]["changeCity_data"])
            propertyShop_res=session.post(url=self.TestData["propertyShop"]["propertyShop_url"],data=self.TestData["propertyShop"]["propertyShop_data"])
            propertyShop_json=json.loads(allData().changeIntoStr(propertyShop_res.text))
            self.assertTrue(propertyShop_res.status_code==200 and len(propertyShop_json["data"])>5)
            Logger(self.TestData["name"]).Info(str(self.TestData["propertyShop"])+'\n'+propertyShop_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test4(self):
        """销售区域接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["changeCity"]["changeCity_url"],data=self.TestData["changeCity"]["changeCity_data"])
            storeArea_res=session.post(url=self.TestData["storeArea"]["storeArea_url"],data=self.TestData["storeArea"]["storeArea_data"])
            storeArea_json=json.loads(allData().changeIntoStr(storeArea_res.text))
            self.assertTrue(storeArea_res.status_code==200 and len(storeArea_json["data"])>5)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()
if __name__=='__main__':
    unittest.main()