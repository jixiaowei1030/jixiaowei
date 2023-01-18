"""
@Time ： 2021/06/22 18:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestExercisesBatchRecord(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_exercises_batch_record(self, xgn_api, data, setupdata):
        """
        desc:测试提交阶段测试题用例
        """

        # 请求接口，获取结果
        actual_res = xgn_api[0].exercises_batch_record(data.batchId, data.exerId, data.exerIndex, data.isAnswered,
                                                       data.isCorrect, data.isCompleted, data.score, data.doTimes,
                                                       data.tryTimes, data.answerContent, setupdata.mobile,
                                                       setupdata.password)

        # assert
        self.assert_equal(0, actual_res.code, "接口断言异常")
        self.assert_true(actual_res.data,"响应异常")
