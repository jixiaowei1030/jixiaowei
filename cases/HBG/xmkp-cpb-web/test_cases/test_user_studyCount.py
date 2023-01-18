"""
@Time ： 2021/3/24 14:40
@Auth ： Aries
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestUserStudyInfo(BaseTestCase):

    def test_user_studyCount(self, cpb_api_scope,setupdata):
        """
        desc:获取用户练环节打卡次数
        steps:
        1、查询用户学习状态,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].user_studyCount(setupdata.mobile,setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        # 第三步：查数据库获取数据库期望结果
        # expect_res = actual_res.data.ticket
        # print(expect_res)
        # 第四步：断言
        # 接口断言
        user_id = cpb_api_scope[3]
        bookId = 2867
        stepType = 3
        redis_key = f"cpbUser:study:{user_id}:{bookId}:{stepType}"
        print(redis_key)
        # 第三步：查数据库获取数据库期望结果
        redis_rsp = cpb_api_scope[2].get(redis_key)
        print(type(redis_rsp), redis_rsp)
        expect_res = int(redis_rsp)
        self.assert_equal(expect_res, actual_res.data, "user_studyCount断言成功")
