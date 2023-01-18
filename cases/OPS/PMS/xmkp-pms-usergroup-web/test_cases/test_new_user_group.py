# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""
import pytest
import time


class Test_new_user_group:
    """
    新建用户分群接口
    """

    @pytest.fixture(scope="function")
    def clear_UserGroup(self, mysql_cli, data):
        t = str(int(time.time() * 1000))
        yield t
        mysql_cli.query(data["teardown"]["query"][0] % t)
        mysql_cli.query(data["teardown"]["query"][1] % t)

    def test_NewUserGroup_Success_Repeat(self, UsergroupWeb_cli, data, clear_UserGroup,setupdata):
        """
        desc:
         case1、新建新概念用户分群，条件logic为and运算
         case2、新建牛津树用户分群，条件logic为or运算
         case3、新建牛津树用户分群所有规则，条件logic为and运算
         case4、新建新概念用户分群所有规则，条件logic为or运算
        steps:
        1、调接口后新建用户分群接口成功
        2、验证返回的状态码为200
        3、数据库或用户分群列表中显示该用户分群名称
        4、重复添加提示用户分群名称已存在
        """
        t = clear_UserGroup
        res = UsergroupWeb_cli.new_userGroup(business=data["business"], groupName=data["groupName"] + t,
                                             rule=data["rule"],mobile=setupdata["mobile"],password=setupdata["password"])
        assert res["code"] == data["assert"]["response"][0]['code']
        assert res["message"] == data["assert"]["response"][0]['message']
        assert res["success"] == data["assert"]["response"][0]['success']
        assert isinstance(res["data"]["groupId"], int)
        res = UsergroupWeb_cli.new_userGroup(business=data["business"], groupName=data["groupName"] + t,
                                             rule=data["rule"],mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"][1]
