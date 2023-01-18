"""
@Time ： 2021/3/18 21:03
@Auth ： wangtao
@File ：test_vip_expire_date.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestVipExpireDate(BaseTestCase):

    def test_vip_expire_date(self, cpb_api_scope,setupdata):
        """
        desc:验证非VIP用户的失效时间是否正确
        steps:
        1、查询接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].vip_expire_date(setupdata.mobile,setupdata.password)
        print(actual_res)
        # 第三二：查数据库获取数据库期望结果
        expect_res = None
        # 第三步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "user_study_info接口调用失败")
        self.assert_equal(expect_res, actual_res.data, "vip用户失效时间错误")