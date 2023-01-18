
"""
@Time ： 2021/4/12 19:55
@Auth ： liulian
@File ：test_bookR_book_star.py
@IDE ：PyCharm
"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestBookRBookStar(BaseTestCase):
    def test_bookR_book_star_1(self, cpb_api_scope, setupdata):
        """
        desc:获取绘本星星数和星星总数（版本迭代逻辑需要更新，听读连三个环节均只有3颗星星）
        steps：
        1.获取用户的response
        2.assert1接口是否请求成功'
        3.assert2绘本等级是否正确
        4.assert3绘本数量是否正确
        """
        # 第1步：请求接口，断言响应
        actual_res = cpb_api_scope[0].bookR_book_star(setupdata.mobile, setupdata.password)
        # 第2步：准备测试数据，获取用户的user_id
        user_id = cpb_api_scope[3]
        print(user_id)
        # 第3步：查询mysql该用户学习计划的绘本等级并做判断
        expect_res = cpb_api_scope[1].query(
                "SELECT * FROM xmkp_child_picture_book.CPB_BOOK_USER_STUDY WHERE user_id ={}".format(user_id), True)
        print(expect_res)
        # 第4步：接口响应成功
        self.assert_equal(0, actual_res.code, "接口调用失败")
        # 第5步：断言库数据与实际返回的星星数与总星星数是否一致
        #（3.8版本迭代逻辑需要更新，听读连三个环节均只有3颗星星）
        print(actual_res.data[0].starTotalCount)
        print(actual_res.data[0].acquiredStarCount)
        #self.assert_equal(expect_res[0], actual_res.data[0].acquiredStarCount, "绘本用户实际获得星星数错误")
        #self.assert_equal(expect_res[0], actual_res.data[0].starTotalCount, "总星星数统计错误")


