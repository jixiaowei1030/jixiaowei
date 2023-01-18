"""
@Time ： 2021/3/4 21:41
@Auth ： wangtao
@File ：test_read_top_detail.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase

@pytest.mark.usefixtures("cpb_api_scope")
class TestReadTopDetail(BaseTestCase):

    def test_read_top_detail_0(self, data, cpb_api_scope, setupdata):
        """
        desc:小朋友都在读，正常返回数据
        steps:
        1、查询获取小朋友都在读的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].read_top_detail(setupdata.mobile, setupdata.password, data.typeId)
        print(actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "read_top_detail_0接口调用失败")

    def test_read_top_detail_1(self, data, cpb_api_scope, setupdata):
        """
        desc:小朋友都在读，正常返回数据
        steps:
        1、查询获取小朋友都在读的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].read_top_detail(setupdata.mobile, setupdata.password, data.typeId)
        print(actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "read_top_detail_1接口调用失败")

    def test_read_top_detail_2(self, data, cpb_api_scope, setupdata):
        """
        desc:小朋友都在读，正常返回数据
        steps:
        1、查询获取小朋友都在读的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].read_top_detail(setupdata.mobile, setupdata.password, data.typeId)
        print(actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "read_top_detail_2接口调用失败")

    def test_read_top_detail_3(self, data, cpb_api_scope, setupdata):
        """
        desc:小朋友都在读，正常返回数据
        steps:
        1、查询获取小朋友都在读的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].read_top_detail(setupdata.mobile, setupdata.password, data.typeId)
        print(actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "read_top_detail_3接口调用失败")

    def test_read_top_detail_4(self, data, cpb_api_scope, setupdata):
        """
        desc:小朋友都在读，正常返回数据
        steps:
        1、查询获取小朋友都在读的接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].read_top_detail(setupdata.mobile, setupdata.password, data.typeId)
        print(actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "read_top_detail_4接口调用失败")
