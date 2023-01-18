"""
@Time ： 2021/3/23 22:35
@Auth ： Aries
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestUserStudyInfo(BaseTestCase):

    def test_vip_card_list(self, cpb_api_scope,setupdata):
        """
        desc:验证获取用户VIP卡列表返回接口信息
        steps:
        1、查询获取用户VIP卡列表返回信息,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].vip_card_list(setupdata.mobile,setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据
        # 第三步：查数据库获取数据库期望结果
        # print(expect_res)
        # 第四步：断言
        # 接口断言
        print(type(actual_res), actual_res.data.vipCardList)
        print(actual_res.data.vipCardList)
        self.assert_is_not_none(actual_res.data.vipCardList, error_msg="vip_card_list接口返回错误")
