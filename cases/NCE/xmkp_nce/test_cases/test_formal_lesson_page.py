"""
@Time ： 2021/06/23 11:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestFormalLessonPage(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_formal_lesson_page(self, xgn_api, data,setupdata):
        """
        desc:测试正式课课程列表
        """

        # 请求
        actual_res = xgn_api[0].formal_lesson_page(data.campId, data.bookType, data.pageNum, data.pageSize,setupdata.mobile, setupdata.password)

        print(actual_res)
        # assert
        self.assert_equal(0, actual_res.code, "接口断言")


