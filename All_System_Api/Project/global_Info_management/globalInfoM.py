#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
import time
class GlobalIM(SuperTest):
    """全局系统接口测试"""
    TestData=read_json('global_management.json')
    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],
                               headers=self.headers)
        self.assertTrue(login_res.status_code==200)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"])+'\n'+login_res.text)
        session.close()

    def test2(self):
        """新建散装商品"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            self.TestData["goodsAdd"]["goodsAdd_data"]["name"]=allData().createGoodName
            goodsAdd_res=session.post(url=self.TestData["goodsAdd"]["goodsAdd_url"],data=self.TestData["goodsAdd"]["goodsAdd_data"])
            self.assertTrue(goodsAdd_res.status_code==200)
            Logger(self.TestData["name"]).Info(str(self.TestData["goodsAdd"])+'\n'+goodsAdd_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    @unittest.skip(u"关联散装商品跳过")
    def test3(self):
        """新建整装商品"""
        pass

    def test4(self):
        """城市信息管理列表展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            getProvince_res=session.post(url=self.TestData["getProvince"]["getProvince_url"],data=self.TestData["getProvince"]["getProvince_data"])
            getProvince_json=json.loads(allData().changeIntoStr(getProvince_res.text))
            self.assertTrue(getProvince_res.status_code==200 and len(getProvince_json["data"])>10)
            Logger(self.TestData["name"]).Info(str(self.TestData["getProvince"])+'\n'+getProvince_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

if __name__=='__main__':
    unittest.main()



