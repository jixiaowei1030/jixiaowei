# -*- coding: utf-8 -*-
"""
@author:bowen jiang
"""

class Test_get_businessSet:
    """
    获取业务集合
    """

    def test_get_businessSet_success(self, ad_ser, data,setupdata):
        """
        desc:成功获取业务集合
        1.调用获取业务集合接口成功
        2.验证返回的状态码为200和返回参数正确
        """

        res = ad_ser.get_businessSet(mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"]