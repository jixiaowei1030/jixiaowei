"""
@Time ： 2021/5/26 14:30
@Auth ： Aries
@File ：test_lately_sentences.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestLatelySentences(BaseTestCase):

    def test_lately_sentences(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取读环节用户最新录音列表接口
        steps:
        1、查询用户学习状态,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].lately_sentences(setupdata.mobile, setupdata.password, book_id=str(data.bookId))
        print(actual_res)
        print(actual_res.data[0].audioUrl)
        # 第二步：准备测试数据
        user_id = cpb_api_scope[3]
        book_id = data["bookId"]
        page_id = actual_res.data[0].pageId
        # 第三步：查数据库获取数据库期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_AUDIO_RECORD_R a WHERE a.user_id={} AND a.book_id={} AND a.page_id={} ORDER BY a.create_time DESC LIMIT 1".format(user_id, book_id,page_id), False)
        print(expect_res)
        print(expect_res.audio_url)
        # 第四步：断言
        # 接口断言
        self.assert_equal('success', actual_res.message, "获取用户最新录音列表接口失败")
        self.assert_equal(actual_res.data[0].audioUrl, expect_res.audio_url, "数据库断言失败")