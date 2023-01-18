# -*- coding: utf-8 -*-
"""
@author:yuanqi
"""

class Test_get_businessTypes_list:
    """
    获取业务类型列表
    """

    def test_get_businessTypes_list_success(self, abtest_cli, data,setupdata):
        """
        desc:成功获取业务类型列表
        1.调用获取业务类型列表接口成功
        2.验证返回的状态码为200和返回参数正确
        """

        res = abtest_cli.get_businessTypes_list(mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"]