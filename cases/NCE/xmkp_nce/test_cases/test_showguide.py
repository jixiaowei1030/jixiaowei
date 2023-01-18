"""
@Time ： 2021/5/24 14:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestShowguide(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_showguide(self,xgn_api,setupdata):
        """
        desc:新用户新手引导用例
        step:
        1、调用接口，获取响应结果
        2、断言结构
        """
        params = 'DRAG_FILL'

        # 获取响应结果
        acturl_res = xgn_api[0].showguide(params, setupdata.mobile, setupdata.password)
        print(acturl_res)

        # assert
        self.assert_equal(0,acturl_res.code,"接口响应异常")
        self.assert_true(acturl_res.data.needGuide, "结果断言异常")
