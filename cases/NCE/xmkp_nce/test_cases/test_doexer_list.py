"""
@Time ： 2021/5/24 14:10
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestDoexerList(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_doexer_list(self, xgn_api, data, setupdata):

        """
        desc:阶段测试答题列表
        step:
        1、获取响应结果
        2、断言
        """

        # 获取响应结果
        acturl_res = xgn_api[0].doexer_list(data.batchId,setupdata.mobile, setupdata.password)
        print(acturl_res)

        # assert
        self.assert_equal(0,acturl_res.code, "接口响应异常")
        self.assert_is_not_none(acturl_res.data, "结果断言异常")
