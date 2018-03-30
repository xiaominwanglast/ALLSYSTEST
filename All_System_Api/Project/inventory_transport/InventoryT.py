#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
import time
class InventTs(SuperTest):
    """仓库运输系统接口测试"""
    TestData=read_json('inventory_transport.json')
    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],
                               headers=self.headers)
        self.assertTrue(login_res.status_code==200)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"])+'\n'+login_res.text)
        session.close()

    def test2(self):
        """尾单波次列表信息显示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            tailList_res=session.post(url=self.TestData["tailList"]["tailList_url"],data=self.TestData["tailList"]["tailList_data"])
            self.assertTrue(tailList_res.status_code==200)
            Logger(self.TestData["name"]).Info(str(self.TestData["tailList"])+'\n'+tailList_res.text)
            self.TestData["createSurplus"]["createSurplus_data"]["orderTime"]=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 5 * 60))
            createSurplus_res=session.post(url=self.TestData["createSurplus"]["createSurplus_url"],data=self.TestData["createSurplus"]["createSurplus_data"])
            createSurplus_json=json.loads(allData().changeIntoStr(createSurplus_res.text))
            self.assertTrue(createSurplus_res.status_code==200 and createSurplus_json['tag'])
            Logger(self.TestData["name"]).Info(str(self.TestData["createSurplus"])+'\n'+createSurplus_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test3(self):
        """波次管理列表信息显示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            expressRoute_res=session.post(url=self.TestData["expressRouteList"]["expressRouteList_url"],data=self.TestData["expressRouteList"]["expressRouteList_data"])
            expressRoute_json=json.loads(allData().changeIntoStr(expressRoute_res.text))
            self.assertTrue(expressRoute_res.status_code==200 and len(expressRoute_json["data"])>10)
            Logger(self.TestData["name"]).Info(str(self.TestData["expressRouteList"])+'\n'+expressRoute_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test4(self):
        """拣货单管理列表信息展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            pickList_res=session.post(url=self.TestData["pickList"]["pickList_url"],data=self.TestData["pickList"]["pickList_data"])
            pickList_json=json.loads(allData().changeIntoStr(pickList_res.text))
            self.assertTrue(pickList_res.status_code==200 and len(pickList_json["data"])>10)
            Logger(self.TestData["name"]).Info(str(self.TestData["pickList"])+'\n'+pickList_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    @unittest.skip(u'参数异常暂不测试')
    def test5(self):
        """库位商品管理列表信息展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            positionGoods_res=session.post(url=self.TestData["positionGoods"]["positionGoods_url"],data=self.TestData["positionGoods"]["positionGoods_data"])
            positionGoods_json=json.loads(allData().changeIntoStr(positionGoods_res.text))
            self.assertTrue(positionGoods_res.status_code==200 and len(positionGoods_json["data"])>10)
            Logger(self.TestData["name"]).Info(str(self.TestData["positionGoods"])+'\n'+positionGoods_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test6(self):
        """司机列表信息展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            courierList_res=session.post(url=self.TestData["courierList"]["courierList_url"],data=self.TestData["courierList"]["courierList_data"])
            courierList_json=json.loads(allData().changeIntoStr(courierList_res.text))
            self.assertTrue(courierList_res.status_code==200 and len(courierList_json["data"])>=1)
            Logger(self.TestData["name"]).Info(str(self.TestData["courierList"])+'\n'+courierList_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test7(self):
        """配送员列表信息展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            deliverList_res=session.post(url=self.TestData["deliverList"]["deliverList_url"],data=self.TestData["deliverList"]["deliverList_data"])
            deliverList_json=json.loads(allData().changeIntoStr(deliverList_res.text))
            self.assertTrue(deliverList_res.status_code==200 and len(deliverList_json["data"])>=1)
            Logger(self.TestData["name"]).Info(str(self.TestData["deliverList"])+'\n'+deliverList_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

if __name__=='__main__':
    unittest.main()


