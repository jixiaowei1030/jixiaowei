"""
@Time ： 2021/4/25 15:25
@Auth ： Aries
@File ：test_top_sentences.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase

@pytest.mark.usefixtures("cpb_api_scope")
class TestTopSentences(BaseTestCase):
    def test_top_sentences(self, cpb_api_scope, setupdata):
        """
        desc:获取用户读环节所有录音
        steps:
        1、查询获取用户读环节所有录音的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].top_sentences(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据，获取用户的user_id
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        user_id = cpb_api_scope[3]
        book_id = 2867
        # 第三步：查数据库获取数据库期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_AUDIO_RECORD_R a WHERE a.user_id ={} And a.book_id={}".format(user_id, book_id), False)
        print(expect_res)
        # 第四步：断言
        # 接口断言
        self.assert_is_not_none(actual_res.data[0], error_msg="test_top_sentences接口返回错误")

        # 数据库断言
        self.assert_is_not_none(expect_res.audio_url, error_msg="test_top_sentences数据库断言失败")

