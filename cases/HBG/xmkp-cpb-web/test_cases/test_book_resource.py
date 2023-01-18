"""
@Time ： 2021/5/26 13:50
@Auth ： durain
@File ：test_book_resource.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase
import json


@pytest.mark.usefixtures("cpb_api_scope")
class TestBookResource(BaseTestCase):
    def test_book_resource(self, cpb_api_scope, setupdata):
        """
        desc:获取某个绘本的详细信息
        steps:
        1、请求阅读理解星星数的接口,获得返回json
        2、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        3、接口断言：接口调用是否成功
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].book_resource(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：数据比对
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_BOOK_R a where a.id=3066")
        print(expect_res)
        self.assert_equal(expect_res.id, actual_res.data.book.id, '绘本id与OPS配置不一致')
        self.assert_equal(expect_res.title, actual_res.data.book.title, '绘本名称与OPS配置不一致')
        self.assert_equal(expect_res.level, actual_res.data.book.level, '绘本等级与OPS配置不一致')
        self.assert_equal(expect_res.is_vip, actual_res.data.book.isVip, '绘本是否vip与OPS配置不一致')
        self.assert_equal(expect_res.has_listen, actual_res.data.book.hasListen, '绘本是否配置听环节与OPS配置不一致')
        self.assert_equal(expect_res.has_exercise, actual_res.data.book.hasExercise, '绘本是否配置练环节与OPS配置不一致')
        self.assert_equal(expect_res.has_read, actual_res.data.book.hasRead, '绘本是否配置读环节与OPS配置不一致')
        self.assert_equal(expect_res.has_see, actual_res.data.book.hasSee, '绘本是否配置看环节与OPS配置不一致')
        # 第三步：接口校验
        self.assert_equal(0, actual_res.code, 'test_book_resource接口响应失败')
        self.assert_equal('success', actual_res.message, 'test_book_resource接口响应失败')
        # key1 = []  # 创建空列表备用
        # key2 = []
        # for key in expect_res:  # 遍历字典a获取key
        #     key1.append(key)
        # print(key1)
        # for key in actual_res.data.book:
        #     key2.append(key)
        # print(key1)
