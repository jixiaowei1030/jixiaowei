"""
@Time ： 2021/3/19 22:15
@Auth ： liulian
@File ：test_listen_win_stars.py
@IDE ：PyCharm

"""

import re
import datetime
import pytest
from utils.tools.base_test_case import BaseTestCase
from utils.common import get_redis


@pytest.mark.usefixture("cpb_api_scope")
class TestListenWinStars(BaseTestCase):
    def test_listen_win_stars_1(self, cpb_api_scope, setupdata):
        """
        desc:验证获取"用户听环节的星星数是否正确"
        steps:
        1、查询"获取听环节星星数"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].listen_win_stars(setupdata.mobile, setupdata.password)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        # 第三步：查询redis数据库，获取数据库的期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER_LISTEN_STAR WHERE book_id='5'and user_id ={}".format(user_id), True)
        # 第四步：断言
        # 断言接口调用是否成功
        # 断言数据库听环节获取的星星数是否正确
        '''print(actual_res.data[0].audioRef)
        print(actual_res.data[0].starCount)
        print(expect_res[0].audio_ref)
        print(expect_res[0].star_count)'''
        if len(actual_res.data) == 0:
            print("用户未阅读该绘本")
            self.assert_equal(0, actual_res.ret, "接口调用失败")
            self.assert_equal("success", actual_res.message, "接口状态错误")
        else:
            for i in range(0, len(actual_res.data)-1):
                self.assert_equal(expect_res[i].audio_ref, actual_res.data[i].audioRef, "听环节获取的绘本页数错误")
                self.assert_equal(expect_res[i].star_count, actual_res.data[i].starCount, "听环节获取的星星数错误")
                self.assert_equal("success", actual_res.message, "获取的星星数错误")
                self.assert_equal(0, actual_res.ret, "接口调用失败")


            



