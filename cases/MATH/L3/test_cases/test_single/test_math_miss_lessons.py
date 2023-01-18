"""
@author:liuzhiyang
"""

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath
import allure

@allure.epic("L3")
class TestMathMissLessons(BaseTestCase):

    def test_math_miss_lessons(self,data,math_client,setupdata):
        '''code': 0, 'msg': '成功'''
        miss_lesson_info=math_client[0].miss_lessons(data.type,setupdata.mobile,setupdata.password)
        self.assert_equal(0, miss_lesson_info.code)
        self.assert_equal('成功', miss_lesson_info['msg'])