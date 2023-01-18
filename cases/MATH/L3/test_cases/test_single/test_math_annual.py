"""
@author:liuzhiyang
"""

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath
import allure


@allure.epic("L3")
class TestMathAnnual(BaseTestCase):

    def test_math_annual1(self,math_client,setupdata):
        '''
        L3年课入口页信息
        '''
        annual_info=math_client[0].annual(setupdata.mobile,setupdata.password)
        self.assert_equal(0,annual_info.code)
        self.assert_equal('成功',annual_info['msg'])
        self.assert_equal('AI年课 S1-S4', annual_info.data.list[0].title)