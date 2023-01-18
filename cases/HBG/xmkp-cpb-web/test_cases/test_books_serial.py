"""
@Time ： 2021/5/26 16:20
@Auth ： Aries
@File ：test_books_serial.py
@IDE ：PyCharm

"""
import re

import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("cpb_api_scope")
class TestBooksSerial(BaseTestCase):

    def test_books_serial(self, cpb_api_scope, setupdata):
        """
        desc:验证全部系列，书架页获取指定系列的绘本的接口
        steps:
        1、查询获取全部系列下获取制定系列的绘本接口,获得返回json
        2、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].books_serial(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        book_id = 6
        # 第三步：查数据库获取数据库期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_BOOK_R a WHERE a.id={}".format(book_id), False)
        print("expect_res", expect_res)
        # 第四步：断言
        # 接口断言
        self.assert_equal('success', actual_res.message, "获取用户最新录音列表接口失败")
        # 数据库断言
        self.assert_equal(expect_res.front_audio_url, actual_res.data[0].frontAudioUrl, "获取用户最新录音列表断言失败")