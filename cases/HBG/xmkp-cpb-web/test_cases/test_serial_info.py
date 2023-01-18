"""
@Time ： 2021/3/18 21:03
@Auth ： wangtao
@File ：test_user_info.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase

@pytest.mark.usefixtures("cpb_api_scope")
class TestUserInfo(BaseTestCase):

    def test_serial_info(self, cpb_api_scope, setupdata):
        """
        desc:全部系列tab获取绘本全部系列名称
        steps:
        1、查询接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].serial_info(setupdata.mobile, setupdata.password)
        print(actual_res)

        #第二步：接口断言
        self.assert_equal(0, actual_res.code, "serial_info接口调用失败")
