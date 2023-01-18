"""
@Time ： 2021/1/26 22:15
@Auth ： wangtao
@File ：test_adConfig_get.py
@IDE ：PyCharm

"""

import pytest
from utils.tools.base_test_case import BaseTestCase



@pytest.mark.usefixture("cpb_api_scope")
class TestPreSalePage(BaseTestCase):

    def test_preSale_page_1(self, cpb_api_scope, setupdata, data):
        """
        desc:验证月卡售前页接口返回正确
        steps:
        1、查询获取月卡售前页的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].preSale_page(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "preSale_page_1接口调用失败")
        # 断言用户的打卡状态是否正确
        self.assert_equal("月卡", actual_res.data.typeName, "返回月卡售前页的接口错误")

    def test_preSale_page_2(self, cpb_api_scope, setupdata, data):
        """
        desc:验证月卡售前页接口返回正确
        steps:
        1、查询获取月卡售前页的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].preSale_page(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "preSale_page_2接口调用失败")
        # 断言用户的打卡状态是否正确
        self.assert_equal("季卡", actual_res.data.typeName, "返回季卡售前页的接口错误")

    def test_preSale_page_3(self, cpb_api_scope, setupdata, data):
        """
        desc:验证月卡售前页接口返回正确
        steps:
        1、查询获取月卡售前页的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].preSale_page(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "preSale_page_3接口调用失败")
        # 断言用户的打卡状态是否正确
        self.assert_equal("年卡", actual_res.data.typeName, "返回年卡售前页的接口错误")

    def test_preSale_page_4(self, cpb_api_scope, setupdata, data):
        """
        desc:验证月卡售前页接口返回正确
        steps:
        1、查询获取月卡售前页的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].preSale_page(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "preSale_page_4接口调用失败")
        # 断言用户的打卡状态是否正确
        self.assert_equal("终身卡", actual_res.data.typeName, "返回终身卡卡售前页的接口错误")
