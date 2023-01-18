"""
@Time ： 2021/06/23 11:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestLessonQuery(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_lesson_query(self, xgn_api, data,setupdata):
        """
        desc:课程进度查询用例
        step:
        1、请求接口，获取响应结果
        2、断言
        """

        # 发起请求
        actual_res = xgn_api[0].lesson_query(data.campId, data.lessonId,setupdata.mobile, setupdata.password)
        print(actual_res)

        # 断言
        self.assert_equal(0,actual_res.code,"接口响应异常")
        self.assert_is_not_none(actual_res.data,"结果断言异常")
