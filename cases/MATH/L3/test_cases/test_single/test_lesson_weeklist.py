"""
@author:liuzhiyang
"""

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath
import allure

@allure.epic("L3")
class TestLessonWeeklist(BaseTestCase):

    def test_lesson_weeklist(self,math_client,data,setupdata):
        """L3所有周的课程"""
        week_info=math_client[0].lesson_weeklist(data.type,setupdata.mobile,setupdata.password)
        self.assert_equal(0, week_info.code)
        self.assert_equal('成功', week_info['msg'])
        self.assert_equal('S1',week_info.data.weekList.data[0].qName)
        self.assert_equal('第1周',week_info.data.weekList.data[0].weekInfo)