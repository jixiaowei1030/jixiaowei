"""
@Time ： 2021/1/28 22:35
@Auth ： wangtao
@File ：test_user_study_info.py
@IDE ：PyCharm

"""
import re
import pytest
from utils.tools.base_test_case import BaseTestCase

@pytest.mark.usefixtures("cpb_api_scope")
class TestResearchQuestionnaireConfig(BaseTestCase):

    def test_research_questionnaire_config(self, cpb_api_scope, setupdata):
        """
        desc:验证获取“调查问卷”的链接是否成功
        steps:
        1、查询获取“调查问卷”的接口,获得返回json
        2、查数据库获得查询数据
        3、接口断言：接口调用是否成功
        4、数据库断言：断言接口返回的重要参数与数据库的值是否一致
        """
        # 第一步：调用接口获取实际响应结果
        actual_res = cpb_api_scope[0].research_questionnaire_config(setupdata.mobile, setupdata.password)
        print(actual_res)
        # 第二步：断言
        # 接口断言
        self.assert_response(actual_res)
        self.assert_not_null(actual_res.data,"查询获取“调查问卷”的接口失败")
