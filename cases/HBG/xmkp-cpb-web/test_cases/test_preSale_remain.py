"""
@Time ： 2021/3/30 14:35
@Auth ： Aries
@File ：test_preSale_remain.py
@IDE ：PyCharm

"""
import pytest

from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestUserStudyInfo(BaseTestCase):

    def test_preSale_remain(self, cpb_api_scope, setupdata):
        """
        desc:验证获取售前页剩余人数接口返回正确
        steps:
        1、查询获取售前页剩余人数接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].preSale_remain(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据
        # 第三步：查数据库获取数据库期望结果
        expect_res = actual_res.data
        print(expect_res)
        # 第四步：断言
        # 接口断言
        print(type(actual_res), actual_res.data)
        print(actual_res.data)
        self.assert_response(actual_res)
        self.assert_is_not_none(actual_res.data, error_msg="preSale_remain接口返回错误")
