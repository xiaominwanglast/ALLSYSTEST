#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
from ddt import ddt,data

@ddt
class MallAS(SuperTest):
    """商城接口测试"""
    TestData=read_json('mall_ApiServer.json')

    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        self.assertTrue(login_res.status_code==200)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"])+'\n'+login_res.text)
        session.close()

    def test2(self):
        """商品分类标题展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            frame_res=session.post(url=self.TestData["frame"]["frame_url"],data=self.TestData["frame"]["frame_data"])
            frame_json=json.loads(allData().changeIntoStr(frame_res.text))
            self.assertTrue(frame_res.status_code==200 and frame_json["data"]["catalog"]>=4)
            Logger(self.TestData["name"]).Info(str(self.TestData["frame"])+'\n'+frame_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test3(self):
        """商品信息信息展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            catalog_res=session.post(url=self.TestData["catalog"]["catalog_url"],data=self.TestData["catalog"]["catalog_data"])
            catalog_json=json.loads(allData().changeIntoStr(catalog_res.text))
            self.assertTrue(catalog_res.status_code==200 and len(catalog_json["data"])>=10)
            Logger(self.TestData["name"]).Info(str(self.TestData["catalog"])+'\n'+catalog_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test4(self):
        """店铺订单信息展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            order_res=session.post(url=self.TestData["userOrder"]["userOrder_url"],data=self.TestData["userOrder"]["userOrder_data"])
            order_json=json.loads(allData().changeIntoStr(order_res.text))
            self.assertTrue(order_res.status_code==200 and order_json["datas"] and order_json["total"]>=20)
            Logger(self.TestData["name"]).Info(str(self.TestData["userOrder"])+'\n'+order_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test5(self):
        """店铺红包可用接口信息"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            cash_res=session.post(url=self.TestData["cash"]["cash_url"],data=self.TestData["cash"]["cash_data"])
            cash_json=json.loads(allData().changeIntoStr(cash_res.text))
            self.assertTrue(cash_res.status_code==200 and cash_json['status']==1)
            Logger(self.TestData["name"]).Info(str(self.TestData["cash"])+'\n'+cash_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test6(self):
        """店铺优惠券可用接口信息"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            code_res=session.post(url=self.TestData["code"]["code_url"],data=self.TestData["code"]["code_data"])
            code_json=json.loads(allData().changeIntoStr(code_res.text))
            self.assertTrue(code_res.status_code==200 and code_json['status']==1)
            Logger(self.TestData["name"]).Info(str(self.TestData["code"])+'\n'+code_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    @data(TestData["login"]["login_data"],TestData["login"]["login_data_pre"])
    def test7(self,value):
        """商城下单[主仓与前置仓]"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=value,headers=self.headers)
        if login_res.status_code==200:
            goodId=0
            catalog_res=session.post(url=self.TestData["catalog"]["catalog_url"],data=self.TestData["catalog"]["catalog_data"])
            catalog_json=json.loads(allData().changeIntoStr(catalog_res.text))
            for goodList in catalog_json["data"]:
                if goodList["left"]>=1000 and goodList["price"]>=30:
                    goodId=goodList["id"]
                    break
            if goodId:
                self.TestData["cartUp"]["cartUp_data"]["command"]=json.dumps([{str(goodId):'add'}])
                session.post(url=self.TestData["cartUp"]["cartUp_url"], data=self.TestData["cartUp"]["cartUp_data"])
                self.TestData["orderPlace"]["orderPlace_data"]["orders"]=json.dumps({str(goodId):1})
                orderPlace_res=session.post(url=self.TestData["orderPlace"]["orderPlace_url"],data=self.TestData["orderPlace"]["orderPlace_data"])
                print orderPlace_res.text
                orderPlace_json=json.loads(allData().changeIntoStr(orderPlace_res.text))
                self.assertTrue(orderPlace_res.status_code==200 and orderPlace_json["status"]==1)
                Logger(self.TestData["name"]).Info(str(self.TestData["orderPlace"])+'\n'+orderPlace_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

if __name__=='__main__':
    unittest.main()

