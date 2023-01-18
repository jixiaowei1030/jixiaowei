"""
@Time ： 2021/06/21 18:10
@Auth ： yanziqiang
"""

import pytest
from common.const import UserToken
from utils.tools.base_test_case import BaseTestCase
import re


class TestNceuserBookList(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_nceuser_book_list(self, xgn_api,setupdata):
        """
        desc:成功查询用户书册列表用例
        1、获取请求结果
        2、断言
        """

        # 获取请求结果
        actual_ids = []
        actual_res = xgn_api[0].nceuser_book_list(setupdata.mobile,setupdata.password)
        data_num = len(actual_res.data)
        for i in range(data_num):
            actual_ids.append(str(actual_res.data[i].id))

        # 获取新概念用户user_id
        user_id = re.search("token=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)

        # 获取数据库结果
        except_res = xgn_api[1].query(
            "select group_concat(distinct(slave_id)) from xmkp_nce.NCE_TABLE_MAPPING as ntm left join xmkp_edu.EDU_CLASSMATE as ec on ntm.master_id = ec.`camp_ref` left join xmkp_nce.NCE_USER as nu on nu.user_id = ec.user_id where ntm.`is_deleted` = 0 and nu.user_id = {}".format(
                user_id), False
        )
        result = except_res.get('group_concat(distinct(slave_id))').split(",")

        # 接口响应断言
        self.assert_equal(0, actual_res.code, "接口响应异常")

        # 数据断言
        self.assert_equal(actual_ids, result, "结果断言异常")
