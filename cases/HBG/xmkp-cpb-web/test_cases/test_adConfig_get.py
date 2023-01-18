"""
@Time ： 2021/1/26 22:15
@Auth ： wangtao
@File ：test_adConfig_get.py
@IDE ：PyCharm

"""
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestAdConfig(BaseTestCase):

    def test_adConfig_get_1(self, cpb_api_scope, setupdata):
        """
        desc:验证h5的轮播图获取是否成功
        steps:
        1、查询获取轮播图的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        #  第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].adConfig_get_1(setupdata.mobile, setupdata.password)
        print(type(actual_res), actual_res)
        #  第二步：查询数据库，获取数据库的期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_AD_CONFIG a WHERE a.type_id = {} AND is_deleted = 0 order by a.id".format(
                "1"),
            True)
        print(expect_res)
        # 第三步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "adConfig_get_1接口调用失败")
        # 断言所有的轮播图URL是否正确
        for i in range(0, len(expect_res)):
            self.assert_equal(actual_res.data[i].linkUrl, expect_res[i].link_url, "轮播图url错误")

    def test_adConfig_get_3(self, cpb_api_scope, setupdata):
        """
        desc:验证结算页的轮播图获取是否成功
        steps:
        1、查询获取轮播图的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        #  第一步：调用接口，获取实际返回数据
        actual_res = cpb_api_scope[0].adConfig_get_3(setupdata.mobile, setupdata.password)
        print(type(actual_res), actual_res)
        #  第二步：查询数据库，获取数据库的期望结果
        expect_res = cpb_api_scope[1].query(
            "SELECT * FROM xmkp_child_picture_book.CPB_AD_CONFIG a WHERE a.type_id = {} AND is_deleted = 0 order by a.id".format(
                "3"),
            True)
        print(expect_res)
        # 第三步：断言
        # 断言接口调用是否成功
        self.assert_equal(0, actual_res.code, "adConfig_get_3接口调用失败")
        # 断言所有的轮播图URL是否正确
        for i in range(0, len(expect_res)):
            self.assert_equal(expect_res[i].link_url, actual_res.data[i].linkUrl, "断言轮播图url错误")
