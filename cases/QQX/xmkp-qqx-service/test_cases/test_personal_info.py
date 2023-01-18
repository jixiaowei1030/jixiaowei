#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 下午5:37
# @Author  : Tina.du
# @File    : test_personal_info.py
import pytest
<<<<<<< HEAD:cases/xmkp-qqx-service/xmkp-qqx-service/test_cases/test_personal_info.py

=======
>>>>>>> d3367dd2070f39f6f35c443b70befb8a14478335:cases/xmkp-qqx-service/test_cases/test_personal_info.py
from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase
import re


@pytest.mark.usefixtures("qqx_api_scope")
class TestPersonalInfo(BaseTestCase):

    def test_query_personal_info(self, qqx_api_scope, setupdata):
        """
        desc: 查询个人信息
        :param qqx_api_scope:
        :return:
        """
        # 第一步：获取个人中心接口响应信息
        personal_res = qqx_api_scope[0].personal_info(setupdata.mobile, setupdata.password)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = re.search("=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)
        
        # 第三步：查询数据库获取用户期望值
        expect_res = qqx_api_scope[1].query(
            f"select * from xmkp_edu.EDU_STUDENT stu where stu.user_id = '{user_id}'", False
        )
        print(expect_res)
        if expect_res:
            # 断言nick_name
            self.assert_equal(expect_res.nick_name, personal_res.data.nickname, "用户UID断言失败")
        else:
            print("没有获取到用户UID")
