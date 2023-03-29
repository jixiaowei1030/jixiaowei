from selenium import webdriver
from time import sleep
import time
from demo.method.org_routing import Org_routing
import unittest
import pytest
from demo_pytest_new.method.org_routing import Org_routing
import allure



# Time Elapsed: 0:06:38.282968-update
class Test_routing():
    test_user_data = [("biqing", "123123")]

    def setup_class(self):
        Test_routing.count = 0
        
    def setup_method(self):
        global driver
        if Test_routing.count > 0:
            driver.refresh()
        else:
            Test_routing.count += 1

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    @pytest.mark.parametrize("login", test_user_data, indirect=True)
    def test_01(self,login):
        '''路由策略信息管理增加，查詢，修改，刪除'''
        global driver
        driver=login
        routing=Org_routing(driver)
        driver.refresh()
        name = "ceshi" + time.strftime("%Y-%m-%d %H")  # 策略名称
        code = "ceshi" + time.strftime("%Y-%m-%d %H")
        name1 = "ceshi1" + time.strftime("%Y-%m-%d %H")  # 策略名称
        code1 = "ceshi1" + time.strftime("%Y-%m-%d %H")
        routing.routing_policy_information_management_add(name,code)
        assert(routing.is_dom_element("添加成功"))  #断言有添加成功提示
        routing.routing_policy_information_management_select(name,code)
        assert(routing.is_dom_element_select(name)) #断言存在要查询的数据
        routing.routing_policy_information_management_update(name1,code1)
        assert(routing.is_dom_element("修改成功"))    #断言有修改成功的提示
        routing.routing_policy_information_management_select(name1, code1)
        routing.routing_policy_information_management_delete()
        assert(routing.is_dom_element("删除成功"))  #断言有删除成功提示

    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def  test_02(self,login):
    #     '''路由映射'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     t=routing.routing_mappingselect("测试1","测试2")
    #     assert(t)         #断言有删除成功的提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_03(self,login):
    #     '''同步映射'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     routing.routing_mapping_synchronous()
    #     assert(routing.is_dom_element_routing_mapping())   #断言已映射，无需同步的提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_04(self,login):
    #     '''标准化结果增加，查询，修改，删除'''
    #     global driver
    #     name="测试"
    #     code="测试"
    #     parameter="测试"
    #     name1 = "测试1"
    #     code1 = "测试1"
    #     parameter1 = "测试1"
    #     driver = login
    #     routing = Org_routing(driver)
    #     routing.standardized_interface_add(name,code,parameter)
    #     assert(routing.is_dom_element("添加成功"))         #断言存在添加成功提示
    #     routing.standardized_interface_select(name,code)
    #     assert(routing.is_dom_element_select(name))   #断言存在要查询的数据
    #     routing.standardized_interface_update(name1,code1,parameter1)
    #     assert(routing.is_dom_element("修改成功"))       #断言存在修改成功提示
    #     routing.standardized_interface_delete()
    #     assert(routing.is_dom_element("删除成功"))       #断言存在删除成功提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_05(self,login):
    #     '''绑定策略'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     t=routing.bandingcelue("测试3","测试3","测试3")
    #     assert(t)              #断言存在删除成功提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_06(self,login):
    #     '''绑定商户策略'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     t=routing.merchant_strategy("测试3","测试3","测试3")
    #     assert(t)              #断言存在删除成功提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_07(self,login):
    #     '''默认路由'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     t=routing.default_routing("银行卡三要素认证","BANK_THREE_VERIFY",3)
    #     assert(t)              #断言存在删除成功提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_08(self,login):
    #     '''明细'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     t=routing.detailed("测试3","测试3","测试3")
    #     assert(t)              #断言存在删除成功提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_09(self,login):
    #     '''配置权重'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     t=routing.configuration_weight("银行卡三要素认证","BANK_THREE_VERIFY")
    #     assert(t)              #断言存在删除成功提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_10(self,login):
    #     '''商户调用策略增加，查询，删除'''
    #     global driver
    #     name = "三要素验证简版(电信运营商)"
    #     driver = login
    #     routing = Org_routing(driver)
    #     routing.call_policyadd(4,4)
    #     routing.call_policyselect(4, name)
    #     routing.call_policydelete()
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_11(self,login):
    #     '''商户调用策略管理商户路由'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     t=routing.merchant_routing(1,"手机在网状态(电信)	")
    #     assert(t)         #断言存在删除成功提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_12(self,login):
    #     '''商户调用策略管理商户权重'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     t=routing.merchant_weight(1,"手机在网状态(电信)")
    #     assert(t)         #断言存在删除成功提示
    #
    # @pytest.mark.parametrize("login", test_user_data, indirect=True)
    # def test_13(self,login):
    #     '''商户调用策略管理智慧路由'''
    #     global driver
    #     driver = login
    #     routing = Org_routing(driver)
    #     routing.merchant_smart_routing(1,"手机在网状态(电信)")
    #     assert(routing.is_dom_element("配置成功"))   #断言存在配置成功提示
    #     t=routing.merchant_current_route()
    #     assert(t)          #断言存在当前路由查看



