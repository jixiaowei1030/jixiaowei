"""
@author:song.zhang
"""
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestAdConfig(BaseTestCase):

    def test_recommend_list(self, cpb_api_scope, setupdata):
        """
        desc:查询用户推荐的列表数据是否正确
        steps:
        1、查询获取用户推荐的列表的接口,获得返回json
        2、数据库断言：接口调用是否成功
        """
        # 1、接口返回的数据
        actual_res = cpb_api_scope[0].recommend_list(setupdata.mobile, setupdata.password)
        for i in range(0, len(actual_res.data.bookList)):
            # 获取book_id
            book_id = actual_res.data.bookList[i].id
            # 2、查询返回的推荐绘本在表里是否存在
            expect_res = cpb_api_scope[1].query(
                "SELECT * FROM xmkp_child_picture_book.CPB_BOOK_R WHERE online  = 1 AND id = {}  order by id".format(
                    book_id), False)
            # 断言
            self.assert_equal(expect_res.id, book_id, error_msg="断言失败：数据库不存在该绘本")
