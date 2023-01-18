"""
@Time ： 2021/3/29 19:55
@Auth ： liulian
@File ：test_cashBack_learnDuration.py
@IDE ：PyCharm
"""
import re
import pytest
from api.http_client_cpb import HttpClientCpb
from utils.log import LOGGER
from utils.tools.base_test_case import BaseTestCase
from utils.common import get_mysql


@pytest.mark.usefixture("cpb_api_scope")
class TestCashBacklearnDuration(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.cpb = HttpClientCpb()
        cls.mysql = get_mysql()

    def teardown_class(cls):
        LOGGER.info("TestWeekReadRecommendPlan类测试结束")

    def test_cashBack_learnDuration_1(self, cpb_api_scope, setupdata, data):
        """
        desc:绘本曝光
        steps：
        1.获取用户的response
        2.assert1接口返回码是否正确是否请求成功
        3.assert2接口是否请求成功
        3.assert3绘本是否曝光
        """
        # 第1步：请求接口，断言响应
        try:
            actual_res = cpb_api_scope[0].cashBack_learnDuration(setupdata.mobile, setupdata.password, data.bookId, data.typeId, data.level)
            print(actual_res)
        except Exception as e:
            raise e
            LOGGER.info("该接口运行失败")
        # 判断该绘本是否曝光
        self.assert_equal(0, actual_res.code, error_msg="接口调用失败")
        self.assert_equal("success", actual_res.message, error_msg="接口调用失败")
        self.assert_equal("success", actual_res.data, error_msg="绘本曝光失败")
