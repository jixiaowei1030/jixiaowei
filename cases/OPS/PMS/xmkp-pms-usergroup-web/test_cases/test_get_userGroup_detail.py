# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""


class Test_get_userGroup_detail:
    """
    获取用户分群详情
    """

    def test_get_userGroup_detail_success(self, UsergroupWeb_cli, data, new_UserGroup,setupdata):
        """
        desc:查询用户用户分群详情
        steps:
        1、调接口用户用户分群详情接口成功
        2、验证返回的状态码为200和返回参数正确
        """
        groupId, t = new_UserGroup
        res = UsergroupWeb_cli.get_userGroup_detail(groupId=groupId,mobile=setupdata["mobile"],password=setupdata["password"])
        assert res["code"] == data["assert"]["response"]["code"]
        assert res["data"]["business"] == data["assert"]["response"]["data"]["business"]
        assert res["data"]["groupName"] == data["assert"]["response"]["data"]["groupName"] % t
        assert res["data"]["rules"] == data["assert"]["response"]["data"]["rules"]
        assert res["data"]["updateFrequency"] == data["assert"]["response"]["data"]["updateFrequency"]
        assert res["data"]["userGroupType"] == data["assert"]["response"]["data"]["userGroupType"]
