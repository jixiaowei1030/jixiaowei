"""
@Time ： 2021/5/14 16:30
@Auth ： liulian
@File ：test_see_win_stars.py
@IDE ：PyCharm
"""
import re
import datetime
import pytest
from utils.tools.base_test_case import BaseTestCase
from utils.common import get_redis
@pytest.mark.usefixture("cpb_api_scope")
class TestSeeWinStars(BaseTestCase):
    def test_see_win_stars_1(self, cpb_api_scope, setupdata):
        """
        desc:验证获取"用户在指定绘本看环节获取的星星详情是否正确"
        steps:
        1、查询"用户在指定绘本看环节获取的星星详情"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].see_win_stars(setupdata.mobile, setupdata.password)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        # 第三步：查询redis数据库，获取数据库的期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER_SEE_STAR WHERE book_id='3023'and user_id ={}".format(
                user_id), True)
        # 第四步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.ret, '接口调用失败')
        # 断言数据库该用户看环节获取的星星数是否正确
        if len(actual_res.data) == 0:
            print('该用户未阅读该绘本的看环节，未获得星星数')
        else:
            for i in range(0, len(expect_res)):
                self.assert_equal(expect_res[i].explore_discovery_ref, actual_res.data[i].exploreDiscoveryRef, "看环节id错误")
                self.assert_equal(expect_res[i].star_count, actual_res.data[i].starCount, "看环节页面对应星星数错误")
                print(expect_res[i].explore_discovery_ref, actual_res.data[i].explore_discovery_ref)