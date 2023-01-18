# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""


class Test_disable_user_group:
    """
     关闭用户分群接口
    """

    def test_disable_user_group_success(self, UsergroupWeb_cli, data, enable_UserGroup,setupdata):
        """
        desc:关闭用户分群规则成功
        steps:
        1、开启用户分群规则
        2、调接口关闭用户分群接口成功
        3、验证返回的状态码为200和返回参数正确
        """
        print(setupdata)
        groupId = enable_UserGroup
        res = UsergroupWeb_cli.disable_userGroup(mobile=setupdata["mobile"],password=setupdata["password"],groupId=groupId,)
        assert res == data["assert"]["response"]
