"""
@Time ： 2021/1/26 22:15
@Auth ： wangtao
@File ：test_adConfig_get.py
@IDE ：PyCharm

"""

import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestLatelyRead(BaseTestCase):

    def test_lately_read_0(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"最近阅读的所有绘本"列表
        steps:
        1、查询"最近阅读的所有绘本"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].lately_read(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：查询redis数据库，获取数据库的期望结果
        # 第三步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "lately_read_0接口调用失败")
        # 断言获取的绘本列表不为空
        self.assert_not_null(actual_res.data, "lately_read_0获取最近阅读的绘本列表为空")

    def test_lately_read_1(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"最近阅读的所有绘本"列表
        steps:
        1、查询"最近阅读的所有绘本"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].lately_read(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：查询redis数据库，获取数据库的期望结果
        # 第三步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "lately_read_1接口调用失败")
        # 断言获取的绘本列表不为空
        self.assert_not_null(actual_res.data, "lately_read_1获取最近阅读的绘本列表为空")

    def test_lately_read_2(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"最近阅读的所有绘本"列表
        steps:
        1、查询"最近阅读的所有绘本"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].lately_read(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：查询redis数据库，获取数据库的期望结果
        # 第三步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "lately_read_2接口调用失败")
        # 断言获取的绘本列表不为空
        self.assert_not_null(actual_res.data, "lately_read_2获取最近阅读的绘本列表为空")

    def test_lately_read_3(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"最近阅读的所有绘本"列表
        steps:
        1、查询"最近阅读的所有绘本"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].lately_read(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：查询redis数据库，获取数据库的期望结果
        # 第三步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "lately_read_3接口调用失败")
        # 断言获取的绘本列表不为空
        self.assert_not_null(actual_res.data, "lately_read_3获取最近阅读的绘本列表为空")

    def test_lately_read_4(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"最近阅读的所有绘本"列表
        steps:
        1、查询"最近阅读的所有绘本"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].lately_read(setupdata.mobile, setupdata.password, data.typeId)
        print(type(actual_res), actual_res)
        # 第二步：查询redis数据库，获取数据库的期望结果
        # 第三步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "lately_read_4接口调用失败")
        # 断言获取的绘本列表不为空
        self.assert_not_null(actual_res.data, "lately_read_4获取最近阅读的绘本列表为空")
