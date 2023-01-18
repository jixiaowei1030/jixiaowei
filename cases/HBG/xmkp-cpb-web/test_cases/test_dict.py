"""
@Time ： 2021/6/15 10:22
@Auth ： felixqian
@File ：test_level_plan.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase

@pytest.mark.usefixture("cpb_api_scope")
class TestLevelPlan(BaseTestCase):

    def test_dict(self, cpb_api_scope, setupdata, data):
        """
        desc:验证获取"分级阅读等级"列表
        steps:
        1、查询"点词查意"列表的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].dict(setupdata.mobile, setupdata.password, word=data.word)
        # print(type(actual_res), actual_res)
        # 第二步：断言
        # 断言接口调用是否成功
        self.assert_response(actual_res)
        self.assert_not_null(actual_res.data.translation)
        actual_translation = actual_res.data.translation
        print(actual_translation)

        # 第三步：数据库断言
        # 断言接口返回的重要参数与数据库的值是否一致
        expect_res = cpb_api_scope[1] \
            .query("SELECT * FROM xmkp_child_picture_book.CPB_DICT WHERE word='{}'".format(data.word), False)
        print(expect_res.translation)
        expect_translation = expect_res.translation.split("\\n")

        for i in range(0, len(actual_translation)):
            self.assert_equal(expect_translation[i],
                              actual_translation[i].type + " " + actual_translation[i].translation, "单词翻译错误")

