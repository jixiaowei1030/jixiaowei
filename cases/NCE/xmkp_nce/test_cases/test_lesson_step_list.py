"""
@Time ： 2021/06/22 14:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestLessonStepDetail(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_lesson_step_list(self, xgn_api, data,setupdata):
        """
        desc:测试体验课学习环节页
        step:
        1、发起请求，获取响应
        2、断言

        """

        # 获取响应结果
        actual_res = xgn_api[0].lesson_step_list(data.campId, data.lessonId,setupdata.mobile, setupdata.password)
        print(actual_res)

        # 断言
        self.assert_equal(0, actual_res.code, "接口响应异常")
        self.assert_is_not_none(actual_res.data.stepList[0], "结果断言失败")


    @pytest.mark.usefixtures("xgn_api")
    def test_lesson_step_list_2(self, xgn_api, data,setupdata):
        """
        desc:测试正式课学习环节页
        step:
        1、发起请求，获取响应
        2、断言

        """

        # 获取响应结果
        actual_res = xgn_api[0].lesson_step_list(data.campId, data.lessonId,setupdata.mobile, setupdata.password)
        print(actual_res)

        # 断言
        self.assert_equal(0, actual_res.code, "接口响应异常")
        self.assert_is_not_none(actual_res.data.stepList[0], "结果断言失败")