"""
@Time ： 2021/6/15 10:22
@Auth ： felixqian
@File ：test_level_plan.py
@IDE ：PyCharm

"""

import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestLevelPlan(BaseTestCase):

    def test_level_plan(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"分级阅读等级"列表
        steps:
        1、查询"分读阅读等级"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].level_plan(setupdata.mobile, setupdata.password, data.level)
        print(type(actual_res), actual_res)
        # 第二步：断言
        # 断言接口调用是否成功
        self.assert_response(actual_res)
        # 断言获取的阅读等级正确
        self.assert_equal(data.level, actual_res.data.level, "阅读等级不匹配")
        # TODO: check redis
