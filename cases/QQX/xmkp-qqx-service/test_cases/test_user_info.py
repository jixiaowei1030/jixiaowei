#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 下午5:22
# @Author  : Tina.du
# @File    : test_user_info.py

import pytest
import re

from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixtures("qqx_api_scope")
class TestUserInfo(BaseTestCase):

    def test_update_user_info(self, qqx_api_scope, data, setupdata):
        """
        desc: 更新用户信息
        steps:
        1、修改用户的信息
        2、获取用户的UID
        3、数据库查询数据
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：获取个人中心接口响应信息
        personal_res = qqx_api_scope[0].update_user_info(data.userInfoShow, data.birthday, data.userSex, data.nickname,
                                                         data.babyHeaderUrl, setupdata.mobile, setupdata.password)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = re.search("=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)

        # 查询数据用户信息
        expect_res = qqx_api_scope[1].query(
            f"select * from xmkp_edu.EDU_STUDENT stu where stu.user_id = '{user_id}'", False
        )
        if personal_res.message == 'success':
            # 断言nick_name
            self.assert_equal(expect_res.nick_name, data.nickname, "用户修改信息错误")
        else:
            print(f'接口请求失败：message:{personal_res.message}')

    def test_query_user_info(self, qqx_api_scope, setupdata):
        """
        desc: 查询用户信息
        steps:
        1、查询用户信息接口
        2、获取用户的UID
        3、数据库查询数据
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：获取个人中心接口响应信息
        personal_res = qqx_api_scope[0].personal_info(setupdata.mobile, setupdata.password)
        # 第二步：准备测试数据，获取用户的user_id
        user_id = re.search("=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)
        
        # 查询数据用户信息
        expect_res = qqx_api_scope[1].query(
            f"select * from xmkp_edu.EDU_STUDENT stu where stu.user_id = '{user_id}'", False
        )
        if personal_res.message == "success":
            # 断言 nick_name 和 headerUrl
            self.assert_equal(personal_res.data.nickname, expect_res.nick_name, "用户昵称不匹配")
            self.assert_equal(personal_res.data.babyHeaderUrl, expect_res.baby_header_url, "用户头像信息不匹配")
        else:
            print(f'接口请求失败：message:{personal_res.message}')
