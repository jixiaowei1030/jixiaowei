"""
@Time ： 2021/3/18 21:02
@Auth ： wangtao
@File ：test_parameter_cocos.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestParameterCocos(BaseTestCase):

    def test_parameter_cocos(self, cpb_api_scope, setupdata):
        """
        desc:验证用户信息是否正确
        steps:
        1、查询接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].parameter_cocos(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        # 第三步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "parameter_cocos接口调用失败")
        self.assert_equal(1073500000101766, actual_res.data.contentId, "返回的skuId错误")
