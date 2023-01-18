"""
@Time ： 2021/6/21 18:00
@Auth ： yanziqiang
"""

import pytest
from utils.tools.base_test_case import BaseTestCase


class TestNceuserEdit(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_nceuser_edit(self, xgn_api, data, setupdata):
        """
        desc:测试修改用户年级 --高中
        1、请求
        2、断言
        """

        # 获取响应结果
        actual_res = xgn_api[0].nceuser_edit(data.grade,setupdata.mobile,setupdata.password)

        # 断言
        self.assert_equal(0, actual_res.code, "断言异常")