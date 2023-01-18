import re
import datetime
import pytest
from utils.tools.base_test_case import BaseTestCase


@pytest.mark.usefixture("cpb_api_scope")
class TestPresaleUrls(BaseTestCase):

    def test_presale_urls_1(self, data, cpb_api_scope, setupdata):
        """
        desc:验证获取售前页的图片是否成功
        steps:
        1、查询获取售前页的图片的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].presale_urls(setupdata.mobile, setupdata.password, data.type)
        print(actual_res)
        # 第四步：断言
        # 接口断言
        self.assert_response(actual_res)
        # 断言
        self.assert_not_null(actual_res.data, "获取售前页的图片失败")

    def test_presale_urls_2(self, data, cpb_api_scope, setupdata):
        """
        desc:验证获取售前页的图片是否成功
        steps:
        1、查询获取售前页的图片的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].presale_urls(setupdata.mobile, setupdata.password, data.type)
        print(actual_res)
        # 第四步：断言
        # 接口断言
        self.assert_response(actual_res)
        # 断言
        self.assert_not_null(actual_res.data, "获取售前页的图片失败")

    def test_presale_urls_3(self, data, cpb_api_scope, setupdata):
        """
        desc:验证获取售前页的图片是否成功
        steps:
        1、查询获取售前页的图片的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].presale_urls(setupdata.mobile, setupdata.password, data.type)
        print(actual_res)
        # 第四步：断言
        # 接口断言
        self.assert_response(actual_res)
        # 断言
        self.assert_not_null(actual_res.data, "获取售前页的图片失败")

    def test_presale_urls_4(self, data, cpb_api_scope, setupdata):
        """
        desc:验证获取售前页的图片是否成功
        steps:
        1、查询获取售前页的图片的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].presale_urls(setupdata.mobile, setupdata.password, data.type)
        print(actual_res)
        # 第四步：断言
        # 接口断言
        self.assert_response(actual_res)
        # 断言
        self.assert_not_null(actual_res.data, "获取售前页的图片失败")

    def test_presale_urls_5(self, data, cpb_api_scope, setupdata):
        """
        desc:验证获取售前页的图片是否成功
        steps:
        1、查询获取售前页的图片的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].presale_urls(setupdata.mobile, setupdata.password, data.type)
        print(actual_res)
        # 第四步：断言
        # 接口断言
        self.assert_response(actual_res)
        # 断言
        self.assert_not_null(actual_res.data, "获取售前页的图片失败")