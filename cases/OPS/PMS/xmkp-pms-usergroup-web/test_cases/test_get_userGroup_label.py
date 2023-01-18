# -*- coding: utf-8 -*-
"""
@author:guwenpeng
"""


class Test_get_userGroup_label:
    """
    查询所有用户分群标签
    """

    def test_get_userGroup_label_success(self, UsergroupWeb_cli, data,setupdata):
        """
        desc:查询用户用户分群所有标签成功
        steps:
        1、调接口用户分群所有标签接口成功
        2、验证返回的状态码为200和返回参数正确
        """

        res = UsergroupWeb_cli.get_userGroup_label(mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"]
