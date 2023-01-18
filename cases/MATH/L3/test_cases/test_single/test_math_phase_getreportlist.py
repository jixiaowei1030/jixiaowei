"""
@author:liuzhiyang
"""

from utils.common import get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath
import allure

@allure.epic("L3")
class TestMathPhaseGetreportlist(BaseTestCase):

    def test_math_phase_getreportlist(self, math_client,setupdata):
        """L3阶段报告，从学习记录页点击阶段报告进入该页面"""
        report_list = math_client[0].phase_get_report_list(setupdata.mobile,setupdata.password)
        i = 1
        for report in report_list.data.reportList:
            self.assert_equal(i, report.qNum)
            self.assert_equal(f'S{i}阶段报告', report.name)
            i += 1
