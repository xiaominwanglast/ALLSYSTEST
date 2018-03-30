#coding:utf-8
#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
import random
import time
class ServiceM(SuperTest):
    """客服系统接口测试"""
    TestData=read_json('service_management.json')
    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],
                               headers=self.headers)
        self.assertTrue(login_res.status_code==200)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"])+'\n'+login_res.text)
        session.close()

    def test2(self):
        """客服审核订单"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            self.TestData["orderList"]["orderList_data"]["start"]=\
                time.strftime('%Y-%m-%d 00:00:00', time.localtime(time.time()))
            self.TestData["orderList"]["orderList_data"]["end"]=\
                time.strftime('%Y-%m-%d 00:00:00', time.localtime(time.time() + 24 * 60 * 60))
            orderList_res=session.get(url=self.TestData["orderList"]["orderList_url"]+"?offset=0&limit=1000&payType=1&order=store&start={0}&end={1}&message=0&timeTag=0".format(
                self.TestData["orderList"]["orderList_data"]["start"],self.TestData["orderList"]["orderList_data"]["end"]))
            orderList_json=json.loads(allData().changeIntoStr(orderList_res.text))
            self.assertTrue(orderList_res.status_code==200 and orderList_json["tag"]=="success")
            Logger(self.TestData["name"]).Info(str(self.TestData["orderList"])+'\n'+orderList_res.text)
            if orderList_json['stores']:
                if orderList_json['stores'][0]['orders']:
                    for order in orderList_json['stores'][0]['orders']:
                        if order['state'] == 0:
                            self.TestData["orderSend"]["orderSend_data"]["orderId"]=int(order['id'])
                            orderSend_res=session.post(url=self.TestData["orderSend"]["orderSend_url"], data=self.TestData["orderSend"]["orderSend_data"])
                            orderSend_json=json.loads(allData().changeIntoStr(orderSend_res.text))
                            self.assertTrue(orderSend_res.status_code==200 and orderSend_json["tag"]=="success")
                            print u'订单号:%s\t 审核通过' % order['id']
                            Logger(self.TestData["name"]).Info(str(self.TestData["orderSend"])+'\n'+orderSend_res.text)
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

    def test3(self):
        """新增退货单"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            branchOrder_res=session.post(url=self.TestData["branchOrder"]["branchOrder_url"],data=self.TestData["branchOrder"]["branchOrder_data"])
            branchOrder_json=json.loads(allData().changeIntoStr(branchOrder_res.text))
            self.assertTrue(branchOrder_res.status_code==200 and len(branchOrder_json["data"])>=20)
            while True:
                StoreGoodsOrderDetail=random.sample(branchOrder_json["data"],1)[0]
                self.TestData["branchOrderDetails"]["branchOrderDetails_data"]["branchOrderId"]=int(StoreGoodsOrderDetail['id'])
                self.TestData["branchOrderDetails"]["branchOrderDetails_data"]["orderId"]=int(StoreGoodsOrderDetail['StoreGoodsOrderId'])
                branchOrderDetails_res=session.post(url=self.TestData["branchOrderDetails"]["branchOrderDetails_url"],data=self.TestData["branchOrderDetails"]["branchOrderDetails_data"])
                branchOrderDetails_json=json.loads(allData().changeIntoStr(branchOrderDetails_res.text))
                self.assertTrue(branchOrderDetails_res.status_code==200 and branchOrderDetails_json["result"])
                branchOrderDetails_json_First=branchOrderDetails_json["result"][0]
                if branchOrderDetails_json_First["amount"]-branchOrderDetails_json_First["returnAmount"]<1:
                    continue
                self.TestData["backGoods"]["backGoods_data"]["backGoodId"]=\
                    int(branchOrderDetails_json_First["GoodId"])
                self.TestData["backGoods"]["backGoods_data"]["branchOrderId"] =\
                    self.TestData["branchOrderDetails"]["branchOrderDetails_data"]["branchOrderId"]
                self.TestData["backGoods"]["backGoods_data"]["detailId"]=\
                    int(branchOrderDetails_json_First["detailId"])
                self.TestData["backGoods"]["backGoods_data"]["goodId"] =\
                    int(branchOrderDetails_json_First["GoodId"])
                self.TestData["backGoods"]["backGoods_data"]["onSellGoodId"]=\
                    int(branchOrderDetails_json_First["OnSellGoodId"])
                self.TestData["backGoods"]["backGoods_data"]["onSellGoodsCombId"]=\
                    int(branchOrderDetails_json_First["OnSellGoodsCombId"])
                self.TestData["backGoods"]["backGoods_data"]["orderId"]=\
                    self.TestData["branchOrderDetails"]["branchOrderDetails_data"]["orderId"]
                self.TestData["backGoods"]["backGoods_data"]["produceDates[]"]=\
                    time.strftime('%Y-%m-%d',time.localtime(time.time()))
                backGoods_res=session.post(url=self.TestData["backGoods"]["backGoods_url"],data=self.TestData["backGoods"]["backGoods_data"])
                backGoods_json=json.loads(allData().changeIntoStr(backGoods_res.text))
                self.assertTrue(backGoods_res.status_code==200 and backGoods_json["tag"]=="success")
                Logger(self.TestData["name"]).Info(str(self.TestData["backGoods"])+'\n'+backGoods_res.text)
                print u"订单编号:%d,已申请退货"%self.TestData["backGoods"]["backGoods_data"]["orderId"]
                break
        else:
            raise Exception(u"登录不成功不进行单元测试")
        session.close()

if __name__=='__main__':
    unittest.main()

