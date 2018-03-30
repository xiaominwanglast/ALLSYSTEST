#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
class PurSalesM(SuperTest):
    """销售系统接口测试"""
    TestData=read_json('purchase_sales_management.json')
    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],
                               headers=self.headers)
        self.assertTrue(login_res.status_code==200)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"])+'\n'+login_res.text)
        session.close()

    def test2(self):
        """库存商品数据显示"""
        session=requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"], data=self.TestData["updateAgency"]["agency_data"],headers=self.headers)
            stockList_res=session.post(url=self.TestData["stockList"]["stockList_url"],data=self.TestData["stockList"]["stockList_data"])
            stockList_json=json.loads(allData().changeIntoStr(stockList_res.text))
            self.assertTrue(stockList_res.status_code==200 and stockList_json["data"] and stockList_json["recordsTotal"]>=20)
            Logger(self.TestData["name"]).Info(str(self.TestData["stockList"])+'\n'+stockList_res.text)
        else:
            raise Exception(u'登录异常不进行单元测试')
        session.close()

    def test3(self):
        """上架商品测试[默认上架140284]"""
        session = requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"], data=self.TestData["updateAgency"]["agency_data"],headers=self.headers)
            publish_Time=allData().create_publish()
            self.TestData["shelvePublish"]["publish_data"]["startTime"]=publish_Time[0]
            self.TestData["shelvePublish"]["publish_data"]["endTime"]=publish_Time[1]
            publish_res=session.post(url=self.TestData["shelvePublish"]["publish_url"],data=self.TestData["shelvePublish"]["publish_data"])
            publish_json=json.loads(allData().changeIntoStr(publish_res.text))
            self.assertTrue(publish_json["status"]==1)
            Logger(self.TestData["name"]).Info(str(self.TestData["shelvePublish"])+'\n'+publish_res.text)
        else:
            raise Exception(u'登录异常不进行单元测试')
        session.close()

    def test4(self):
        """入驻商第三方信息列表"""
        session=requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"], data=self.TestData["updateAgency"]["agency_data"],headers=self.headers)
            suppliers_res=session.post(url=self.TestData["suppliers"]["suppliers_url"],data=self.TestData["suppliers"]["suppliers_data"])
            suppliers_json=json.loads(allData().changeIntoStr(suppliers_res.text))
            self.assertTrue(suppliers_res.status_code==200 and suppliers_json["data"] and suppliers_json["status"]==1)
            Logger(self.TestData["name"]).Info(str(self.TestData["suppliers"])+'\n'+suppliers_res.text)
        else:
            raise Exception(u'登录异常不进行单元测试')
        session.close()

    def test5(self):
        """起送费设置"""
        session=requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"], data=self.TestData["updateAgency"]["agency_data"],headers=self.headers)
            baseDelivery_res=session.post(url=self.TestData["baseDelivery"]["baseDelivery_url"],data=self.TestData["baseDelivery"]["baseDelivery_data"])
            baseDelivery_json=json.loads(allData().changeIntoStr(baseDelivery_res.text))
            self.assertTrue(baseDelivery_res.status_code==200 and baseDelivery_json["status"]==1)
            Logger(self.TestData["name"]).Info(str(self.TestData["baseDelivery"])+'\n'+baseDelivery_res.text)
        else:
            raise Exception(u'登录异常不进行单元测试')
        session.close()

    def test6(self):
        """优惠券列表信息显示"""
        session=requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"], data=self.TestData["updateAgency"]["agency_data"],headers=self.headers)
            getCoupons_res=session.post(url=self.TestData["getCoupons"]["getCoupons_url"],data=self.TestData["getCoupons"]["getCoupons_data"])
            getCoupons_json=json.loads(allData().changeIntoStr(getCoupons_res.text))
            self.assertTrue(getCoupons_res.status_code==200 and getCoupons_json["data"] and getCoupons_json["recordsTotal"]>=20)
            Logger(self.TestData["name"]).Info(str(self.TestData["getCoupons"])+'\n'+getCoupons_res.text)
        else:
            raise Exception(u'登录异常不进行单元测试')
        session.close()

if __name__=='__main__':
    unittest.main()

