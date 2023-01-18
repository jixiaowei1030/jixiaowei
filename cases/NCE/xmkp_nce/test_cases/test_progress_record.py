"""
@Time ： 2021/6/22 14:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase

class TestProgressRecord(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_progress_record(self,xgn_api,data,setupdata):
        """
        desc:课程进度记录用例
        step:
        1、调用接口，获取响应结果
        2、断言
        """

        # response
        actual_res = xgn_api[0].progress_record(data.studyStepId, data.bpType, data.status,
                                                data.breakpoint, setupdata.mobile, setupdata.password)
        print(actual_res)

        # assert
        self.assert_equal(0,actual_res.code,"接口响应异常")
        self.assert_true(actual_res.data,"结果断言异常")

    @pytest.mark.usefixtures("xgn_api")
    def test_progress_record_2(self,xgn_api,data, setupdata):
        """
        desc:阶段测试课程进度记录用例
        step:
        1、调用接口，获取响应结果
        2、断言
        """

        # response
        actual_res = xgn_api[0].progress_record(data.studyStepId, data.bpType, data.status,
                                                data.breakpoint, setupdata.mobile, setupdata.password)
        print(actual_res)

        # assert
        self.assert_equal(0,actual_res.code,"接口响应异常")
        self.assert_true(actual_res.data,"结果断言异常")