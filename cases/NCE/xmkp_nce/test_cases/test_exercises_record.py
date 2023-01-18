"""
@Time ： 2021/5/24 14:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestExercisesRecord(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_exercises_record(self,xgn_api,data,setupdata):
        """
        desc:用户练习题记录用例
        step:
        1、请求接口获取响应结果
        2、断言：结果断言
        """
        # 请求接口，获取返回结果
        actual_res = xgn_api[0].exercises_record(data.campRef, data.lessonRef, data.stepRef, data.exercisesRef,
                                                 data.originAudioUrl, data.type, data.text, data.isCorrrect,
                                                 data.score, data.audioUrl, data.duration, data.tryTimes, data.doTimes,
                                                 data.isCompleted, data.answerContent,
                                                 setupdata.mobile, setupdata.password)
        print(actual_res)

        # assert
        self.assert_equal(0,actual_res.code,"接口响应异常")
        self.assert_equal(1,actual_res.data.addGold,"获取金币异常")