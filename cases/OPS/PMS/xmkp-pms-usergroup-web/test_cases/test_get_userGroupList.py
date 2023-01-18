# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""


class Test_get_userGroupList:
    """
    查询所有用户分群标签
    """

    def test_get_userGroup_by_page(self, UsergroupWeb_cli, data,setupdata):
        """
        desc:分页查询用户分群
        steps:
        1、分页查询用户分群成功
        2、验证返回的状态码为200和返回参数正确
        """

        res = UsergroupWeb_cli.get_userGroup_by_page(current=str(data["current"]),
                                                     pageSize=str(data["pageSize"]), pageNum=str(data["pageNum"]),
                                                     mobile=setupdata["mobile"],password=setupdata["password"])
        assert len(res["data"]["list"]) == data["response"]["data.len"]
        assert res["data"]["pageNum"] == data["response"]["data.pageNum"]
        assert res["data"]["total"] >= data["response"]["data.total"]
