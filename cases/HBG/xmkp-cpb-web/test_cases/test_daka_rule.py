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
class TestDakaRule(BaseTestCase):

    def test_daka_rule_0(self, cpb_api_scope, setupdata):
        """
        desc:验证获取"打卡规则提示"是否正确）
        steps:
        1、查询"打卡规则提示"列表的接口,获得返回json
        2、接口断言：接口调用是否成功
        3、接口断言：返回的打卡规则提示文案是否正确
        """
        # 第1步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].daka_rule(setupdata.mobile, setupdata.password)
        print(type(actual_res.data[0]))
        print(type(actual_res.data[1]))
        # 第2步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "打卡规则提示test_daka_rule接口返回状态码错误")
        self.assert_equal("success", actual_res.message, "打卡规则提示test_daka_rule接口返回信息错误")
        # 断言配置的打卡规则提示文案是否正确
        if actual_res.data is not None:
            self.assert_equal("当天完成一本新绘本的阅读或者复习已读绘本的任意三个环节，即可打卡成功", actual_res.data[0], "打卡规则提示的文案错误")
            self.assert_equal("在该卡有效期内，可参与打卡286天，全额返现活动", actual_res.data[1], "打卡规则提示的文案错误")
        else:
            print("打卡规则提示文案未配置")