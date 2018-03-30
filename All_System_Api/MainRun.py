#coding:utf-8
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import time
from BaseRequest.BasePath import result_path
from BaseRequest.BasePath import log_path
from Public.readJson import removeAll
from Public import HTMLTestRunnerCN
from Project.purchase_sales_management.purchaseSalesManagement import PurSalesM
from Project.mall_ApiServer.MallApiS import MallAS
from Project.service_management.serverMana import ServiceM
from Project.inventory_transport.InventoryT import InventTs
from Project.global_Info_management.globalInfoM import GlobalIM
from Project.store_management.storeMana import StoreM
from Project.purchase_management.purchaseMana import PurchaseM
def do_TestUnit():
    print u'--------------开始执行测试用例----------------'
    testSuit=unittest.TestSuite()
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(PurSalesM))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(MallAS))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ServiceM))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(InventTs))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(GlobalIM))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreM))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(PurchaseM))
    #清空测试log与报告
    for path in [log_path,result_path]:
        removeAll(path)
    #定义个报告存放路径，支持相对路径
    # now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    # print u'开始时间',now
    filename =result_path+'\\'+"HTML"+"-result.html"
    fp = file(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=u'店达系统自动化测试报告',description=u'详细测试报告:')
    #运行测试用例
    runner.run(testSuit)
    fp.close()
    end=time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    print u'结束时间',end
if __name__=="__main__":
    do_TestUnit()