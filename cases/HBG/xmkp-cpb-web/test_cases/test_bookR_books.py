"""
@Time ： 2021/1/28 22:35
@Auth ： wangtao
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestBookRBooks(BaseTestCase):

    def test_bookR_books(self, cpb_api_scope, setupdata):
        """
        desc:验证书架页获取绘本列表是否成功
        steps:
        1、查询获取书架页获取绘本列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].bookR_books(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：查数据库获取数据库期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_BOOK_R  where id = {}".format(2867), False)
        print(expect_res)
        # 第三步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "bookR_books接口调用失败")
        # 数据库断言
        actual_res =[ item.id for item in actual_res.data] # 获取书架页列表所有book_id
        self.assert_in(expect_res.id,actual_res,"bookR_books接口返回列表中不存在2867的绘本")
