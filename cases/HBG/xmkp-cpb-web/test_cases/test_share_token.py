
import re
import pytest
from utils.tools.base_test_case import BaseTestCase

@pytest.mark.usefixtures("cpb_api_scope")
class TestShareToken(BaseTestCase):

    def test_share_token(self, cpb_api_scope, data, setupdata):
        """
        desc:验证站外分享页获取token是否成功
        steps:
        1、查询获取token的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].share_token(setupdata.mobile, setupdata.password, data.uid, data.bookId)
        print(actual_res)
        # 第四步：断言
        # 接口断言
        self.assert_response(actual_res)
        # 断言
        self.assert_not_null(actual_res.data, "站外分享页获取token失败")


