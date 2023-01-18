"""
@Time ： 2021/3/18 21:03
@Auth ： wangtao
@File ：test_user_info.py
@IDE ：PyCharm

"""

import re
import pytest
from utils.tools.base_test_case import BaseTestCase

@pytest.mark.usefixtures("cpb_api_scope")
class TestUserInfo(BaseTestCase):

    def test_user_info(self, cpb_api_scope, setupdata):
        """
        desc:验证用户信息是否正确
        steps:
        1、查询接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].user_info(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：准备测试数据，获取用户的user_id
        # user_id = re.search("=(.*?)&", services.m_token["Cookie"]).group(1)
        user_id = cpb_api_scope[3]
        # 第三步：查数据库获取数据库期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_USER a WHERE a.user_id ={}".format(user_id), False)
        print(expect_res)
        # 第四步：断言
        # 接口断言
        self.assert_equal(0, actual_res.code, "user_info接口调用失败")
        # 数据库断言
        self.assert_equal(expect_res.user_id, actual_res.data.userId, "用户UID断言失败")