"""
@author:liuzhiyang
"""

from utils.common import  get_mysql
from utils.tools.base_test_case import BaseTestCase
from api.http_client_math import HttpClientMath
import allure

@allure.epic("L3")
class TestMathLessonProcess(BaseTestCase):

    def test_math_lesson_process(self,math_client,data,setupdata):
        """L3用户当前学习课程，最近一次开课的课程信息，从首页点击进入学习请求该接口"""
        process_info=math_client[0].lesson_process(data.type,setupdata.mobile,setupdata.password)
        self.assert_equal(0,process_info.code)
        self.assert_equal('成功',process_info.msg)
        self.assert_in('lessonSeq',process_info.data)
        self.assert_in('url',process_info.data.practiceList[0])
        self.assert_in('startImg', process_info.data.practiceList[1])
        self.assert_in('moduleIcon', process_info.data.practiceList[2])