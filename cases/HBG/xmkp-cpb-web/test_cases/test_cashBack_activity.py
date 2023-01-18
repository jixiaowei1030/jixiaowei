"""
@Time ： 2021/3/24 11:40
@Auth ： Aries
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestUserStudyInfo(BaseTestCase):

    def test_cashBack_activity(self, cpb_api_scope, setupdata):
        """
        desc:获取用户学习状态
        steps:
        1、查询用户学习状态,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].cashBack_activity(setupdata.mobile, setupdata.password)
        # 第二步：准备测试数据
        user_id = cpb_api_scope[3]
        # 第三步：查数据库获取数据库期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_CASH_BACK_USER_ACTIVITY WHERE user_id ={}".format(user_id), False)
        #print(expect_res.activity_type)
        # 第四步：断言
        # 接口断言
        #print(type(actual_res), actual_res.data[0].activityType)
        print(type(actual_res))
        print(type(expect_res))
        print(actual_res.data)
        if not actual_res.data:
            print("该用户没有学习，并不存在学习状态")
        elif actual_res.data[0].activityStatus == 0:
            print("该用户为已参与活动")