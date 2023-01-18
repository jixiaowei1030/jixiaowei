# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""


class Test_enable_user_group:
    """
     开启用户分群接口
    """

    def test_enable_user_group_success(self, UsergroupWeb_cli, data, new_UserGroup,setupdata):
        """
        desc:开启用户分群
        steps:
        1、调接口启用用户分群接口成功
        2、验证返回的状态码为200和返回参数正确
        """
        groupId,t = new_UserGroup
        res = UsergroupWeb_cli.enable_userGroup(groupId=groupId,mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"]
