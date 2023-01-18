# -*- coding: utf-8 -*-
"""
@author:bowen jiang
"""

class Test_get_ad_vendorSet:
    """
    获取广告引擎集合
    """

    def test_get_ad_vendorSet_success(self, ad_ser, data,setupdata):
        """
        desc:成功获取广告引擎集合
        1.调用获取广告引擎集合接口成功
        2.验证返回的状态码为200和返回参数正确
        """
        res = ad_ser.get_ad_vendorSet(mobile=setupdata["mobile"],password=setupdata["password"])
        assert res == data["assert"]["response"]