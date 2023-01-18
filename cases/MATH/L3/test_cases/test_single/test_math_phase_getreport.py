"""
@author:liuzhiyang
"""
import allure

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath



@allure.epic("L3")
class TestMathPhaseGetreport(BaseTestCase):

    @allure.title('{data.casename}')
    def test_math_phase_getreport(self,math_client,data,setupdata):
        """L3获取阶段报告详情"""
        report_info=math_client[0].phase_get_report(data.qNum,setupdata.mobile,setupdata.password)
        self.assert_equal(0,report_info.code)
        self.assert_equal('成功',report_info.msg)
        self.assert_in('lessonCount',report_info.data.reportData)