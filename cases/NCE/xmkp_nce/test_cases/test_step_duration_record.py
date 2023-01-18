"""
@Time ： 2021/6/22 19:10
@Auth ： yanziqiang
"""

import pytest
from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase
import re


class TestStepDurationRecord(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_step_duration_record(self, xgn_api, data,setupdata):
        """
        desc:学习环节学习时长记录测试用例
        steps:
        1、请求接口，返回结果
        2、断言
        """

        # 获取响应结果
        actual_res = xgn_api[0].exercises_duration_record(data.studyStepId, data.duration, setupdata.mobile,
                                                          setupdata.password)
        print(actual_res)

        # 获取新概念用户user_id
        user_id = re.search("token=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)

        # 获取前置学习时长
        ori_time = xgn_api[1].query(
            "select sum(duration) from xmkp_nce.NCE_STUDY_STEP_DURATION where user_id = {} and study_step_id = {}".format(
                user_id, data.studyStepId), False)


        # 获取当前学习时长
        cur_time = xgn_api[1].query(
            "select sum(duration) from xmkp_nce.NCE_STUDY_STEP_DURATION where user_id = {} and study_step_id = {}".format(
                user_id, data.studyStepId), False)

        # 断言
        self.assert_equal(0, actual_res.code, "接口断言异常")
        # self.assert_equal(data.duration, cur_time["sum(duration)"] - ori_time["sum(duration)"], "结果断言异常")
