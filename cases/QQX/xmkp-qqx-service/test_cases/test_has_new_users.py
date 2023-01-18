#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 下午10:42
# @Author  : Tina.du
# @File    : test_has_new_users.py
<<<<<<< HEAD:cases/xmkp-qqx-service/xmkp-qqx-service/test_cases/test_has_new_users.py

=======
# @Project description：用户-首页判断是否新用户，以及售前页连接
>>>>>>> d3367dd2070f39f6f35c443b70befb8a14478335:cases/xmkp-qqx-service/test_cases/test_has_new_users.py
import re

import pytest

from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("qqx_api_scope")
class TestHasNewUser(BaseTestCase):

    def test_has_new_user(self, qqx_api_scope, setupdata):
        """
        desc: 首页判断是否新用户，以及售前页连接
        steps:
        1、修改用户的信息
        2、获取用户的UID
        3、数据库查询数据
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：获取个人中心接口响应信息
        personal_res = qqx_api_scope[0].has_new_user(setupdata.mobile, setupdata.password)
        print(personal_res)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = re.search("=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)
        # 查询数据用户信息
        expect_res = qqx_api_scope[1].query(
            f"select * from xmkp_edu.EDU_STUDENT stu where stu.user_id = '{user_id}'", False
        )
        self.assert_equal(personal_res.message, "success", "接口断言失败")

        if personal_res.data.hasClassmate:
            self.assert_equal(str(personal_res.data.uid), user_id, "用户UID断言失败")
        else:
            print(expect_res)
