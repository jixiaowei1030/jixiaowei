"""
@Time ： 2021/06/22 19:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase
import re


class TestExperienceLessonList(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_experience_lesson_list(self, xgn_api, data,setupdata):
        """
        desc:测试体验课课程列表
        1、获取请求结果
        2、断言
        """

        # 请求
        actual_res = xgn_api[0].experience_lesson_list(data.campId, data.bookType,setupdata.mobile, setupdata.password)

        print(actual_res)
        # 断言
        self.assert_equal(0, actual_res.code, "接口响应断言异常")

