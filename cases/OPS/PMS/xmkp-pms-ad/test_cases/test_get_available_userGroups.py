# -*- coding: utf-8 -*-
"""
@author:bowen jiang
"""
class Test_get_available_userGroups:
    """
    查询所有可用分群(人群包)
    """
    def test_get_available_userGroups_success(self, ad_ser, data,setupdata):
        """
        desc:成功查询所有可用分群(人群包)
        1.调用查询所有可用分群(人群包)接口成功
        2.验证返回的状态码为200和返回参数正确
        """
        res = ad_ser.get_available_userGroups(mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"]