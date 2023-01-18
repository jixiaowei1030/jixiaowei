"""
@Time ： 2021/06/22 14:10
@Auth ： yanziqiang
"""
import pytest
from utils.tools.base_test_case import BaseTestCase


class TestLessonStepDetail(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_lesson_step_detail(self, xgn_api, data,setupdata):
        """
        desc:测试体验课warm up环节
        step:
            1、发起请求获取请求结果
            2、断言
        """
        # 获取响应结果
        actual_res = xgn_api[0].lesson_step_detail(data.stepId, data.campId,data.startDate,setupdata.mobile, setupdata.password)
        print(actual_res)

        # assert
        self.assert_equal(0, actual_res.code, "接口响应异常")
        self.assert_equal(data.stepId, actual_res.data.stepId, "结果断言异常")

    @pytest.mark.usefixtures("xgn_api")
    def test_lesson_step_detail_2(self, xgn_api, data,setupdata):
        """
        desc:测试体验课lecture环节
        step:
            1、发起请求获取请求结果
            2、断言
        """
        # 获取响应结果
        actual_res = xgn_api[0].lesson_step_detail(data.stepId, data.campId,data.startDate,setupdata.mobile, setupdata.password)
        print(actual_res)

        # assert
        self.assert_equal(0, actual_res.code, "接口响应异常")
        self.assert_equal(data.stepId, actual_res.data.stepId, "结果断言异常")

    # @pytest.mark.usefixtures("xgn_api")
    # def test_lesson_step_detail_3(self, xgn_api, data,setupdata):
    #     """
    #     desc:测试体验课report环节
    #     step:
    #         1、发起请求获取请求结果
    #         2、断言
    #     """
    #     # 获取响应结果
    #     actual_res = xgn_api[0].lesson_step_detail(data.stepId, data.campId,data.startDate,setupdata.mobile, setupdata.password)
    #     print(actual_res)
    #
    #     # assert
    #     self.assert_equal(0, actual_res.code, "接口响应异常")
    #     self.assert_equal(data.stepId, actual_res.data.stepId, "结果断言异常")
