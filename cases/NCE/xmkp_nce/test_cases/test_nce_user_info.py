"""
@Time ： 2021/06/21 18:10
@Auth ： yanziqiang
"""

import pytest
import re
from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase


class TestNceuserInfo(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_nceuser_info(self,xgn_api,setupdata):
        """
        desc:获取用户信息用例
        steps：
        1、获取请求结果
        2、断言
        """

        # 请求接口获取响应结果
        actual_res = xgn_api[0].nceuser_info(setupdata.mobile,setupdata.password)

        # 获取user_id
        user_id = re.search("token=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)

        # 数据库取值
        mysql_user_info = xgn_api[1].query("select * from xmkp_nce.NCE_USER where user_id ={}".format(user_id), False)

        print(actual_res)
        # 断言
        self.assert_equal(0,actual_res.code,"接口请求异常")
        self.assert_equal(actual_res.data.userId, mysql_user_info.user_id,"数据校验异常")
