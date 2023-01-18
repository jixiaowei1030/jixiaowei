"""
@Time ： 2021/5/26 13:50
@Auth ： durain
@File ：test_reading_comprehension_stars.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase
import json


@pytest.mark.usefixtures("cpb_api_scope")
class TestReadingComprehensionStars(BaseTestCase):
    def test_reading_comprehension_stars(self, cpb_api_scope, setupdata):
        """
        desc:验证听环节阅读理解已获得星星数
        steps:
        1、请求阅读理解星星数的接口,获得返回json
        2、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        3、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].reading_comprehension_stars(setupdata.mobile, setupdata.password)
        print(actual_res.data)
        # 第二步：准备测试数据，获取用户的user_id
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        user_id = cpb_api_scope[3]
        print(user_id)
        # 第三步：数据比对
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_BOOK_USER_STUDY WHERE book_id='3066' and user_id ={}".format(
                user_id), True)
        if expect_res[0].reading_comprehension_star == 3:
            self.assert_equal(expect_res[0].win_reading_comprehension_star, actual_res.data.starCount, "获取用户该绘本阅读理解星星数失败")
            print('该绘本已配置阅读理解且用户已获得阅读理解星星数为3')
        else:
            print('该绘本听环节未配置阅读理解')
        # 第四步：接口断言
        self.assert_equal('success', actual_res.message, "test_reading_comprehension_stars接口调用失败")
        self.assert_equal(0, actual_res.code, "test_reading_comprehension_stars接口响应码错误")
