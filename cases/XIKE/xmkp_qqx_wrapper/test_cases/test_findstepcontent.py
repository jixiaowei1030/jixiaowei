"""
@author:lhz
"""


from utils.tools.base_test_case import BaseTestCase
import allure
import time


@allure.epic("bookworm")
class TestBookWormFindStepContent(BaseTestCase):
    """
                    desc:根据环节id获取内容
                    steps:
                    1、查询环节id的接口,获得返回json
                    2、接口断言：2.1返回code为0，
                               2.2msg为success，

                    """
    @allure.title("{data.casename}")
    def test_bookworm_find_step_content(self, xike_client, data, setupdata):
        """根据环节id获取内容"""
        # 第一步：调用接口，获取返回结果
        get_stepContent = xike_client[0].find_step_content(data.stepId, setupdata.mobile, setupdata.password)
        # print(get_stepContent)
        # 第二步：断言
        self.assert_equal(0, get_stepContent.code)
        self.assert_equal("success", get_stepContent.message)
        self.assert_equal("86b8c4886e6540239eabf6eedcbc0753", get_stepContent.data.indexId)

    @allure.title("{data.casename}")
    def test_bookworm_find_step_content_with_wrong_stepId(self, xike_client, data, setupdata):
        """根据错误的环节id获取内容"""
        # 第一步：调用接口，获取返回结果
        get_stepContent = xike_client[0].find_step_content(data.stepId, setupdata.mobile, setupdata.password)
        # print(get_stepContent)
        # 第二步：断言
        self.assert_equal(0, get_stepContent.code)
        self.assert_equal("success", get_stepContent.message)
        self.assert_is_none(get_stepContent.data)

    @allure.title("{data.casename}")
    def test_bookworm_find_step_content_with_empty_string(self, xike_client, data, setupdata):
        """环节id为空字符串"""
        # 第一步：调用接口，获取返回结果
        get_stepContent = xike_client[0].find_step_content(data.stepId, setupdata.mobile, setupdata.password)
        # print(get_stepContent)
        # 第二步：断言
        self.assert_equal(0, get_stepContent.code)
        self.assert_equal("success", get_stepContent.message)
        self.assert_is_none(get_stepContent.data)

    @allure.title("{data.casename}")
    def test_bookworm_find_step_content_with_int_stepid(self, xike_client, data, setupdata):
        """环节id为数字"""
        # 第一步：调用接口，获取返回结果
        get_stepContent = xike_client[0].find_step_content(data.stepId, setupdata.mobile, setupdata.password)
        # print(get_stepContent)
        # 第二步：断言
        self.assert_equal(0, get_stepContent.code)
        self.assert_equal("success", get_stepContent.message)
        self.assert_is_none(get_stepContent.data)

