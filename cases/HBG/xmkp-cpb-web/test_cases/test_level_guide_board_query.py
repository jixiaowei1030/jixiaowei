"""
@Time ： 2021/6/15 13:49
@Auth ： felixqian
@File ：test_level_guide_query.py
@IDE ：PyCharm

"""

import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestLevelGuideBoardQuery(BaseTestCase):

    def test_level_guide_board_query_1(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"分级牌与路牌"列表
        steps:
        1、查询"分级牌与路牌"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].level_guide_board_query(setupdata.mobile, setupdata.password, data.type)
        print(actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_response(actual_res)
        # 断言
        self.assert_not_null(actual_res.data, "test_level_guide_board_query等级牌信息为空")

        expect_res = cpb_api_scope[1]\
            .query("SELECT * FROM xmkp_child_picture_book.CPB_LEVEL_GUIDE_BOARD_INFO WHERE type = '1'", True)

        print(expect_res)

    def test_level_guide_board_query_2(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"分级牌与路牌"列表
        steps:
        1、查询"分级牌与路牌"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].level_guide_board_query(setupdata.mobile, setupdata.password, data.type)
        print(actual_res)
        # 第二步：断言
        self.assert_response(actual_res)
        # 断言接口调用是否成功
        self.assert_not_null(actual_res.data, "test_level_guide_board_query路牌信息为空")

        expect_res = cpb_api_scope[1] \
            .query("SELECT * FROM xmkp_child_picture_book.CPB_LEVEL_GUIDE_BOARD_INFO WHERE type = '2'", True)
