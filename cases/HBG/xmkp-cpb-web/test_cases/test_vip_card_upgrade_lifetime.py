"""
@Time ： 2021/6/3 11:26
@Auth ： liulian
@File ：test_daka_rule.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestVipCardUpGradeLifeTime(BaseTestCase):

    def test_vip_card_upgrade_lifetime_0(self, cpb_api_scope,setupdata):
        """
        desc:验证获取"用户是否有购买终身卡的权益"接口是否正确）
        steps:
        1、查询"用户是否有购买终身卡的权益"列表的接口,获得返回json
        2、接口断言：接口调用是否成功
        3、接口断言：用户是否具有升级终身卡权益
        """
        # 第1步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].vip_card_upgrade_lifetime(setupdata.mobile,setupdata.password)
        print(actual_res)
        print(actual_res.data.type)
        # 第2步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "打卡规则提示test_daka_rule接口返回状态码错误")
        self.assert_equal("success", actual_res.message, "打卡规则提示test_daka_rule接口返回信息错误")
        # 断言用户是否有否买终身卡的权益
        if actual_res.data.type == 0:
            self.assert_equal(True, actual_res.data.success, "该用户有购买终身卡的权益")
            print("该用户有购买终身卡权益，可以购买终身卡")
        elif actual_res.data.type == 1:
            self.assert_equal(False, actual_res.data.success, "该用户没有购买终身卡的权益")
            print("该用户已经购买过终身卡，无法再次购买终身卡")
        else:
            # self.assert_equal("false", actual_res.data.success, "该用户没有购买终身卡的权益")
            print("该用户不含有未过期的年卡或者三年卡，无法购买终身卡")

