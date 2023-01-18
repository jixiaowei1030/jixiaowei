"""
@author:liuzhiyang
"""
import allure


from utils.tools.base_test_case import BaseTestCase




@allure.epic("L3")
class TestMathLessonInfo(BaseTestCase):


    @allure.title('{data.casename}')
    def test_math_lesson_info(self,data,math_client,setupdata):
        '''L3课程信息'''
        lesson_info=math_client[0].lesson_info(data.id,setupdata.mobile,setupdata.password)
        if data.id<=340:
            self.assert_equal(data.img,lesson_info.data.img)
        else:
            self.assert_equal(data.status,500)
