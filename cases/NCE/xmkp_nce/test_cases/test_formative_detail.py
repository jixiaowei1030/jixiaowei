"""
@Time ： 2021/06/23 14:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestFormativeDetail(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_formative_detail(self,xgn_api,data,setupdata):
        """
        desc:进入阶段测试课程用例
        step:
        1、请求接口，获取响应结果
        2、断言
        """

        # 获取响应结果
        actual_res = xgn_api[0].formative_detail(data.lessonId, data.campId,data.startDate,setupdata.mobile, setupdata.password)
        print(actual_res)

        # assert
        self.assert_equal(0,actual_res.code,"接口响应异常")
        self.assert_is_not_none(actual_res.data.exercisesList[0],"结果断言异常")