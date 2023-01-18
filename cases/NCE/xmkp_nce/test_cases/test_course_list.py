"""
@Time ： 2021/6/21 18:00
@Auth ： yanziqiang
"""

import pytest
# from common.apollo import services
from utils.tools.base_test_case import BaseTestCase
import re
from common.const import UserToken


class TestCourseList(BaseTestCase):

    @pytest.mark.usefixtures("xgn_api")
    def test_course_list(self, xgn_api,setupdata):
        """
        desc:用户端登陆后获取训练营信息
        steps:
        1、请求接口获取响应结果
        2、获取数据库实际结果
        3、断言：结果断言，数据库期望值断言
        """
        actual_camps = []

        # 获取响应结果,提取训练营名称
        actual_res = xgn_api[0].course_list(setupdata.mobile,setupdata.password)
        camp_num = len(actual_res.data)
        for i in range(camp_num):
            actual_camps.append(actual_res.data[i].campTitle)



        # 获取新概念用户user_id
        user_id = re.search("token=(.*?)&", UserToken.USERTOKEN["Cookie"]).group(1)

        # 获取数据库值
        expect_camps = xgn_api[1].query(
            "select group_concat(camp_title) from xmkp_edu.EDU_CAMP as t left join xmkp_edu.EDU_CLASSMATE as k on t.id = k.camp_ref where k.user_id = {}".format(
                user_id), False
        )
        # 结果转列表
        result = expect_camps.get('group_concat(camp_title)').split(',')

        print(result)
        print(actual_camps)

        # 接口响应断言
        self.assert_equal(0, actual_res.code, "接口响应异常")

        # 数据库断言
        self.assert_equal(result.sort(), actual_camps.sort(), "数据校验异常")
