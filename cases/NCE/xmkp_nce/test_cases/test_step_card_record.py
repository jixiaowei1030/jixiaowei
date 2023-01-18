"""
@Time ： 2021/5/28 18:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestStepCardRecord(BaseTestCase):


    @pytest.mark.usefixtures("xgn_api")
    def test_step_card_record(self,xgn_api,data,setupdata):
        """
        desc:学习环境卡片状态记录用例
        """

        # 获取响应结果
        actual_res = xgn_api[0].step_card_record(data.studyStepId, data.cardId, data.stepId, setupdata.mobile, setupdata.password)

        # 断言
        self.assert_equal(0,actual_res.code,"接口响应异常")