"""
@Time ： 2021/6/15 13:36
@Auth ： felixqian
@File ：test_level_read.py
@IDE ：PyCharm

"""

import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestLevelRead(BaseTestCase):

    def test_level_read(self, cpb_api_scope, setupdata):
        """
        desc:验证获取"分级阅读绘本"列表
        steps:
        1、查询"分级阅读绘本"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].level_read(setupdata.mobile, setupdata.password)
        print(actual_res.data)
        # 第2步：断言
        # 断言接口调用是否成功
        self.assert_response(actual_res)
        self.assert_equal("success", actual_res.message, "打卡规则提示test_level_read接口返回信息错误")
        self.assert_not_null(actual_res.data, "test_level_read获取最近阅读的绘本列表为空")
        # TODO: check redis
