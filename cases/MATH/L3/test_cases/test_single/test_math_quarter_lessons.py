"""
@author:liuzhiyang
"""

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath
import allure

@allure.epic("L3")
class TestQuarterLessons(BaseTestCase):

    def test_math_quarter_lessons(self,math_client,data,setupdata):
        '''
        code': 0, 'msg': '成功'''
        annual_info=math_client[0].quarter_lessons(data.quarterId,setupdata.mobile,setupdata.password)
        self.assert_equal(0,annual_info.code)
        self.assert_equal('成功',annual_info['msg'])